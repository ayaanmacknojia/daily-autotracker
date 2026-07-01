import json

morning_or_evening = input("Are you running this in the morning or evening? Warning: if two identical times of the day are inputted consecutively, data will be null for other time of day (m/e): ")
message_for_morning = None

# initialize variables with 'None' in case user skips morning/evening prompts 
sleep_hours = None
gym_today = None 
waking_mood = None
goal_today = None

win_today = None
hours_worked = None
mood_evening = None
goal_achieved = None
message_for_morning = None

stats_dict = {}

try:
    with open("daily_data.json", "r") as file:
        stats_dict = json.load(file)
        sleep_hours = stats_dict["sleep_hours"]
        gym_today = stats_dict["gym_today"]
        waking_mood = stats_dict["waking_mood"]
        goal_today = stats_dict["goal_today"]

except FileNotFoundError:
    pass


if morning_or_evening == "m":
    print("--- MORNING SYSTEM CHECK ---")

    # gathering morning inputs
    sleep_hours = input("How many hours did you sleep last night? ")
    gym_today = input("Gym today? (y/n): ")
    waking_mood = input("How do you feel after waking up? ")
    goal_today = input("What is one goal for today? ")

    # print morning summary
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

    #print full day summary
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


# add all stats to dictionary
stats_dict["sleep_hours"] = sleep_hours
stats_dict["gym_today"] = gym_today
stats_dict["waking_mood"] = waking_mood
stats_dict["goal_today"] = goal_today

stats_dict["win_today"] = win_today
stats_dict["hours_worked"] = hours_worked
stats_dict["mood_evening"] = mood_evening
stats_dict["goal_achieved"] = goal_achieved
stats_dict["morning_message"] = message_for_morning


# dump dictionary object to json text file
with open("daily_data.json", "w") as file:
    json.dump(stats_dict, file)

'''
with open("day_save.txt", "a") as file:

    file.write("\n\n[FULL DAY SUMMARY]\n")
    file.write("Morning:\n")
    file.write(f"Hours slept: {sleep_hours} hr\n")
    file.write(f"Gym session today: {gym_today}\n")
    file.write(f"Mood after waking: {waking_mood}\n")
    file.write(f"Today's goal: {goal_today}\n")


    file.write("\nEvening:\n")
    file.write(f"Today's win: {win_today}\n")
    file.write(f"Hours worked today: {hours_worked} hr\n")
    file.write(f"Mood tonight: {mood_evening}\n")
    file.write(f"Today's goal achieved: {goal_achieved}\n")
'''


