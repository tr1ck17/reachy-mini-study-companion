from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
import time

questions = [
	{"question": "What is 2 + 3?", "answer": "5"},
	{"question": "What is 5 + 1?", "answer": "6"},
	{"question": "What is 3 + 4?", "answer": "7"},
]

def wave(mini):
	mini.goto_target(
		head=create_head_pose(yaw=15, degrees=True),
		duration=0.5
	)
	mini.goto_target(
		head=create_head_pose(yaw=-15, degrees=True),
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
		wave(mini)
		speak(mini, "Hello! Let's practice math together!")

		for question in questions:
			speak(mini, question["question"])

			user_answer = input("Your Answer: ").strip()

			if user_answer == question["answer"]:
				speak(mini, "That's correct! Great Job!")
			else:
				speak(mini, "Not quite, but that's okay!")

		speak(mini, "You did a great job today. Come back soon!")
		wave(mini)

if __name__ == "__main__":
	run_demo()