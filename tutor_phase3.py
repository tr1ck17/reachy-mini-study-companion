from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
import time

questions = [
	{"question": "What is 2 + 3?", "answer": "5"},
	{"question": "What is 5 + 1?", "answer": "6"},
	{"question": "What is 3 + 4?", "answer": "7"},
]

def greeting(mini):
	mini.goto_target(
		antennas=[0.6, -0.6], duration=0.3
	)
	mini.goto_target(
		antennas=[-0.6, 0.6], duration=0.3
	)
	
	mini.goto_target(
		antennas=[0, 0],
		duration=1.0
	)

def nod(mini):
	mini.goto_target(
		head=create_head_pose(pitch=30, degrees=True),
		duration=0.25
	)
	mini.goto_target(
		head=create_head_pose(pitch=-30, degrees=True),
		duration=0.25
	)
	mini.goto_target(
		head=create_head_pose(pitch=30, degrees=True),
		duration=0.25
	)
	mini.goto_target(
		head=create_head_pose(pitch=0, degrees=True),
		duration=0.25
	)

def shake(mini):
	mini.goto_target(
		head=create_head_pose(yaw=45, degrees=True),
		duration=0.5
	)
	mini.goto_target(
		head=create_head_pose(yaw=-45, degrees=True),
		duration=0.5
	)
	mini.goto_target(
		head=create_head_pose(yaw=0, degrees=True),
		duration=0.6
	)

def speak(mini, text):
	print(f"[REACHY]: {text}")

def run_demo():
	with ReachyMini() as mini:
		incorrect_answers = []
		greeting(mini)
		speak(mini, "Hey There! Let's practice math together!")

		for question in questions:
			speak(mini, question["question"])
			user_answer = input("Your Answer: ").strip()

			if user_answer == question["answer"]:
				nod(mini)
				speak(mini, "That's correct! Great job!")
			else:
				shake(mini)
				speak(mini, "Not quite, but it's okay!")
				incorrect_answers.append(question)
		
		if incorrect_answers:
			speak(mini, "Let's review some of the questions that you missed.")
			for question in incorrect_answers:
				speak(mini, question["question"])
				user_answer = input("Your answer: ").strip()

				if user_answer == question["answer"]:
					nod(mini)
					speak(mini, "That's correct this time!")
				else:
					shake(mini)
					speak(mini, f"The correct answer is {question['answer']}.")
		speak(mini, "You did a great job today. Come back soon!")
		greeting(mini)

if __name__ == "__main__":
	run_demo()