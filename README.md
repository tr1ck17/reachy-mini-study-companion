REACHY MINI STUDY COMPANION

This project displays a (currently) very basic adapative tutoring model using the Reachy Mini (as of right now, designed for the simulated model)

Questions asked by the bot are adjusted according to the streak of correct answers the participant has answered

The adaptive difficulty is based in this way:
  easy -> medium -> hard

Reachy has some gestures that show encouragement, agreement, or guided direction:
  Nods for correct answers
  Shakes for incorrect answers
  Wiggling Antennas for greeting and goodbyes

Incorrect questions are stored in a list and repeated at the end of the session

To run this:
Using Powershell (like me):
  Install uv (Python package manager for easy installation)
    Command: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  Close Powershell, open new terminal, and check for version to ensure installation went well
    Command: uv --version
  Install python
    Command: uv python install 3.12 --default
  Download and install Git for windows:
    Command: git lfs install
  Create virtual environment:
    WARNING: Move INTO the project directory before creating virtual environemnt, ex: cd reachy-mini-study-companion (after cloning inside the directory you want)
    Command: uv venv reachy_mini_env --python 3.12
  Activate the environment:
      WARNING: Before activation in powershell, open powershell as admin and run: powershell Set-ExecutionPolicy RemoteSigned
      Then close admin window
    Command: reachy_mini_env\Scripts\activate
  Install simulation module:
    Command: uv pip install "reachy-mini[mujoco]"
  To begin running simulation:
    Command: reachy-mini-daemon --sim
  Then, create code file, or use one above, and run it with:
    python file.py
