from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
import time

def wave(mini):
	mini.goto_target(antennas=[0.6, -0.6], duration=0.3)
	mini.goto_target(antennas=[-0.6, 0.6], duration=0.3)
	mini.goto_target(antennas=[0, 0], duration=0.3)

def nod(mini):
    mini.goto_target(head=create_head_pose(pitch=15, degrees=True), duration=0.6)
    time.sleep(0.2)
    mini.goto_target(head=create_head_pose(pitch=-5, degrees=True), duration=0.6)
    time.sleep(0.2)
    mini.goto_target(head=create_head_pose(pitch=0, degrees=True), duration=0.4)

def shake(mini):
    mini.goto_target(head=create_head_pose(yaw=15, degrees=True), duration=0.4)
    mini.goto_target(head=create_head_pose(yaw=-15, degrees=True), duration=0.4)
    mini.goto_target(head=create_head_pose(yaw=0, degrees=True), duration=0.3)

def speak(mini, text):
	print(f"[REACHY]: {text}")

easy_questions = [
    {"question": "What is 2 + 3?", "answer": "5"},
    {"question": "What is 5 + 1?", "answer": "6"},
    {"question": "What is 3 + 4?", "answer": "7"},
]

medium_questions = [
    {"question": "What is 12 - 4?", "answer": "8"},
    {"question": "What is 6 x 3?", "answer": "18"},
]

hard_questions = [
    {"question": "What is 15 ÷ 3?", "answer": "5"},
    {"question": "What is 7 x 6?", "answer": "42"},
]

def run_adaptive_demo():
	student_profile = {
		"correct": 0,
		"incorrect": 0,
		"streak": 0
	}
	
	with ReachyMini() as mini:
		wave(mini)
		speak(mini, "Hello! Let's practice some math!")

		all_questions = easy_questions.copy()

		incorrect_answers = []

		for question in all_questions:
			speak(mini, question["question"])
			user_answer = input("Your Answer: ").strip()

			if user_answer == question["answer"]:
				nod(mini)
				speak(mini, "That's correct! Good job!")
				student_profile["correct"] += 1
				student_profile["streak"] += 1
			else:
				shake(mini)
				speak(mini, f"Not quite, the correct answer is {question['answer']}.")
				student_profile["incorrect"] += 1
				student_profile["streak"] = 0
				incorrect_answers.append(question)

			if student_profile["streak"] >= 3:
				speak(mini, "Wow! You're on a roll! Let's try something a bit harder!")
				all_questions += medium_questions

			if student_profile["incorrect"] >= 2:
				speak(mini, "Let's slow down and review the tricky questions")
				student_profile["incorrect"] = 0

		if incorrect_answers:
			speak(mini, "Let's go over the missed questions.")
			for question in incorrect_answers:
				speak(mini, question["question"])
				user_answer = input("Your Answer: ").strip()
				if user_answer == question["answer"]:
					nod(mini)
					speak(mini, "That's correct this time!")
				else:
					shake(mini)
					speak(mini, f"The correct answer is {question['answer']}.")

		speak(mini, "Great work today! Come back soon for more math fun!")
		wave(mini)

if __name__ == "__main__":
	run_adaptive_demo()