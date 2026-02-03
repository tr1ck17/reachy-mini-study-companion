# imports will vary between sim and wireless/wired model

from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose
import numpy as np
import time

questions = [
	{"question": "What is 2 + 3?", "answer": "5"},
	{"question": "What is 5 + 1?", "answer": "6"},
	{"question": "What is 3 + 4?", "answer": "7"},
]

# gestures

def wave():
	print("[GESTURE] Wave")
def nod():
	print("[GESTURE] Wave")
def shake():
	print("[GESTURE] Wave")
def speak(text):
	print(f"[REACHY SAYS]: {text}")
	time.sleep(1)

# main demo
def run_demo():
	use reachymini as a mini:
	wave()
	speak("Hey there! Let's practice some math!")

	for question in questions:
		speak(question["question"])
		
		user_answer = input("Your Answer: ").strip()	# strip for answer

		if user_answer == question["answer"]:
			nod()
			speak("Great job, that's correct!")
		else:
			shake()
			speak("Not quite, but that's okay!")
	speak("Great job today! Come back again when you're ready for more!")
	wave()

if __name__ == "__main__":
	run_demo()