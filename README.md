# daily-autotracker

A command-line habit tracker that logs morning and evening check-ins (sleep, gym, mood, goals, etc) and stores them to a local JSON file. It also generates weekly summaries about certain habits like sleep and tracks the user's daily login streak.

## How to run
python tracker.py

## Built with
- Python 3
- JSON module

## 2 bug fixes
  - Fixed edge-case for very first run of program where streak_check function would start looking for non-existent, previously entered data by implementing a guard to return function early
  - Fixed logic issue where program would ask whether today's goal was achieved even if user skipped the morning run by implementing a check to see whether today's goal existed before asking for its completion

## Screenshot
<img width="1448" height="726" alt="image" src="https://github.com/user-attachments/assets/390ebb02-368b-463a-b354-e42f6209dc83" />
