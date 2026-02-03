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
    {"question": "2 + 3?", "answer": "5"},
    {"question": "5 + 1?", "answer": "6"},
    {"question": "3 + 4?", "answer": "7"},
]

medium_questions = [
    {"question": "12 - 4?", "answer": "8"},
    {"question": "6 x 3?", "answer": "18"},
    {"question": "15 ÷ 3?", "answer": "5"},
]

hard_questions = [
    {"question": "7 x 6?", "answer": "42"},
    {"question": "18 ÷ 2?", "answer": "9"},
    {"question": "13 + 29?", "answer": "42"},
]

difficulty_levels = ["easy", "medium", "hard"]
def get_questions_for_streak(streak):
	if streak < 3:
		return easy_questions
	elif streak < 6:
		return medium_questions
	else:
		return hard_questions

def run_fully_adaptive_demo():
	student_profile = {
		"correct": 0,
		"incorrect": 0,
		"streak": 0
	}
	
	incorrect_answers = []

	with ReachyMini() as mini:
		wave(mini)
		speak(mini, "Hello! Let's practice some math together!")

		session_active = True

		while session_active:
			current_questions = get_questions_for_streak(student_profile["streak"])
			for question in current_questions:
				speak(mini, question["question"])
				user_answer = input("Your Answer: ").strip()

				if user_answer == question["answer"]:
					nod(mini)
					speak(mini, "Correct! Well done!")
					student_profile["correct"] += 1
					student_profile["streak"] += 1
					student_profile["incorrect"] = 0
				else:
					shake(mini)
					speak(mini, f"Oops! The correct answer is {question['answer']}.")
					student_profile["incorrect"] += 1
					student_profile["streak"] = 0
					incorrect_answers.append(question)

				if student_profile["streak"] > 0 and student_profile["streak"] % 3 == 0:
					speak(mini, "Great! Let's try some harder questions!")
				if student_profile["incorrect"] >= 2:
					speak(mini, "Let's slow down and review some tricky ones.")
					student_profile["incorrect"] = 0
			if student_profile["streak"] >= 9:
				session_active = False

		if incorrect_answers:
			speak(mini, "Let's review the questions you missed.")
			for question in incorrect_answers:
				speak(mini, question["question"])
				user_answer = input("Your Answer: ").strip()
				if user_answer == question["answer"]:
					nod(mini)
					speak(mini, "Correct this time! Good job!")
				else:
					shake(mini)
					speak(mini, f"The correct answer is {question['answer']}.")
		speak(mini, "Great work today! Come back soon for more math practice!")
		wave(mini)

if __name__ == "__main__":
	run_fully_adaptive_demo()	