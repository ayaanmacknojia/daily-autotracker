morning_or_evening = input("Are you running this in the morning or evening? Warning: if two identical times of the day are inputted consecutively, data will be null for other time of day (m/e): ")
message_for_morning = None

# initialize variables with 'None' in case user skips morning prompts 
sleep_hours = None
gym_today = None 
waking_mood = None
goal_today = None

if morning_or_evening == "m":
    print("--- MORNING SYSTEM CHECK ---")

    # gathering morning inputs
    sleep_hours = input("How many hours did you sleep last night? ")
    gym_today = input("Gym today? (y/n): ")
    waking_mood = input("How do you feel after waking up? ")
    goal_today = input("What is one goal for today? ")

    print("\n\n[MORNING STATS SUMMARY]")
    print(f"Hours slept: {sleep_hours} hr")
    print(f"Gym session today: {gym_today}")
    print(f"Mood after waking: {waking_mood}")
    print(f"Today's goal: {goal_today}")
else:
    print("--- EVENING SYSTEM CHECK ---")

    # gathering evening inputs
    win_today = input("What is one win from today? ")
    hours_worked = input("How many hours did you work today? ")
    mood_evening = input("How do you feel after today? ")
    goal_achieved = input("Was today's goal achieved? (y/n) ")
    message_for_morning = input("Leave a message for tomorrow: ")

    print("\n\n[FULL DAY SUMMARY]")
    print("Morning:")
    print(f"Hours slept: {sleep_hours} hr")
    print(f"Gym session today: {gym_today}")
    print(f"Mood after waking: {waking_mood}")
    print(f"Today's goal: {goal_today}")


    print("\nEvening:")
    print(f"Today's win: {win_today}")
    print(f"Hours worked today: {hours_worked} hr")
    print(f"Mood tonight: {mood_evening}")
    print(f"Today's goal achieved: {goal_achieved}")

    




