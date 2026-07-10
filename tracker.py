import json # for data storage that remains after exiting app
from datetime import datetime, timedelta # for calculations involving dates # for using time and dates

# weekly summary function: finds avg sleep, total gym days, goal hit rate, etc
def summarize(data_file):
    date_dict = data_file

    total_sleep = 0
    gym_days = 0
    goal_hit = 0
    total_hours_worked = 0

    sleep_counter = 0
    work_counter = 0
    goal_counter = 0

    sleep_avg = 0
    goal_hit_rate = 0
    avg_hours_worked = 0

# loop over outer dictionary for date (key) and data (value -> nested dictionary)
    for date, data in date_dict.items():
        print(f"Date: {date}")

        # loop over inner dictionary for data calculations and printing summary
        for key, value in data.items():
            if key == "sleep_hours":
                print(f"Sleep hours: {value}")
                total_sleep += value
                sleep_counter += 1
            elif key == "gym_today" and value == "y":
                print(f"Gym today: {value}")
                gym_days += 1
            elif key == "waking_mood":
                print(f"Waking mood: {value}")
            elif "goal_today" in data and key == "goal_achieved" and value == "y":
                print(f"Goal {data['goal_today']} was achieved!")
                goal_hit += 1
                goal_counter += 1
            elif "goal_today" in data and key == "goal_achieved" and value == "n":
                print(f"Goal {data['goal_today']} was not achieved.")
                goal_counter += 1
            elif key == "goal_today":
                print(f"Goal today: {value}")
            elif key == "win_today":
                print(f"Win today: {value}")
            elif key == "hours_worked":
                print(f"Hours worked: {value}")
                total_hours_worked += value
                work_counter += 1
            elif key == "mood_evening":
                print(f"Evening mood: {value}")
            
    
    # calculate relevant data for averages/numbers
    if sleep_counter > 0:
        sleep_avg = round(total_sleep / sleep_counter, 2)
    if goal_counter > 0:
        goal_hit_rate = round((goal_hit / goal_counter) * 100, 2)
    if work_counter > 0:
        avg_hours_worked = round(total_hours_worked / work_counter, 2)

    print("--- FINAL SUMMARY ---")
    print(f"Average hours slept: {sleep_avg}")
    print(f"Gym days this week: {gym_days}")
    print(f"Goal hit rate: {goal_hit_rate} % of goals are hit!")
    print(f"Average hours worked per day: {avg_hours_worked}")

# streak check function     
def streak_check(data_file):
    date_dict = data_file

    date_today = datetime.today().date()
    last_date_string = list(date_dict)[-1] # get previous entry date, not yesterday's date (no guarantee of one day gap)
    last_entry_date = datetime.strptime(last_date_string, "%Y-%m-%d").date()
    last_entry_stats = list(date_dict.values())[-1]  # get previous entry's stats_dict

    streak_yesterday = last_entry_stats.get("streak", 0) # uses .get() in case no streak exists for yesterday (first run ever)

    day_difference = (date_today - last_entry_date).days

    if day_difference == 1: # one day apart -> increment previous streak
        stats_dict["streak"] = streak_yesterday + 1
    elif day_difference > 1: # multiple days apart -> reset streak to 1 (includes today)
        stats_dict["streak"] = 1
    else: # 0 or negative days apart, do nothing (this prevents a morning run to evening run from incrementing twice per day)
        pass

# function to ensure user inputs m/e for morning_or_evening variable
def morning_evening(prompt_text):
    while True:
        try:
            user_choice = input(prompt_text).strip().lower() # eliminate whitespace, convert to lowercase 

            if user_choice not in ['m', 'e']:  # detect if input is correct
                raise ValueError("Invalid entry. You must type in eiher 'm' or 'e'.") # 'raise' jumps to except block with error message
            
            return user_choice # return user's choice back to variable if input was correct
        
        except ValueError as error: 
            print(error)


# function to ensure user inputs y/n for some variables
def yes_or_no(prompt_text):
    while True:
        try:
            user_choice = input(prompt_text).strip().lower()

            if user_choice not in ['y', 'n']:  # detect if input is correct
                raise ValueError("Invalid entry. You must type in eiher 'y' or 'n'.") 
            
            return user_choice # return user's choice back to variable if input was correct
        
        except ValueError as error: 
            print(error)

# function to ensure user inputs numbers for some variables
def numerical_check(prompt_text):
    while True:
        try:
            user_num = float(input(prompt_text).strip())  # float automcatically crashes if input is not a float
            return user_num # return user's number back to variable if input was correct
        
        except ValueError: 
            print("Invalid entry. Please enter a valid number/decimal.")


morning_or_evening = morning_evening("Are you running this in the morning or evening? Warning: if two identical times of the day are inputted consecutively, data won't exist for other time of day (m/e): ")
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



stats_dict = {} # user stats dictionary
date_dict = {} # dictionary that holds user stats dictionary

'''
yesterday_with_time = datetime.now() - timedelta(days=1) # get yesterday's date
yesterday_date_string = yesterday_with_time.strftime("%Y-%m-%d") # convert to string
'''

date = datetime.now()
string_date = date.strftime("%Y-%m-%d")

# load in previous file if possible to preserve previous data
try: 
    with open("daily_data.json", "r") as file:
        date_dict = json.load(file)
        if string_date in date_dict:
            stats_dict = date_dict[string_date] # set stats_dict to hold previously added values
except (FileNotFoundError, json.JSONDecodeError): # if file not found OR file found but is empty
    pass



if morning_or_evening == "m": # morning input
    print("--- MORNING SYSTEM CHECK ---")

    # gathering morning inputs
    sleep_hours = numerical_check("How many hours did you sleep last night? ")
    gym_today = yes_or_no("Gym today? (y/n): ")
    waking_mood = input("How do you feel after waking up? ")
    goal_today = input("What is one goal for today? ")

    # print morning summary
    print("\n\n[MORNING STATS SUMMARY]")
    print(f"Hours slept: {sleep_hours} hr")
    print(f"Gym session today: {gym_today}")
    print(f"Mood after waking: {waking_mood}")
    print(f"Today's goal: {goal_today}")

    date_yesterday = date - timedelta(days=1)
    string_date_yesterday = date_yesterday.strftime("%Y-%m-%d")
    if string_date_yesterday in date_dict:
        if "morning_message" in date_dict[string_date_yesterday]:
            print(f"A message you left yourself yesterday: {date_dict[string_date_yesterday]['morning_message']}")

    # add all morning stats to dictionary
    stats_dict["sleep_hours"] = sleep_hours
    stats_dict["gym_today"] = gym_today
    stats_dict["waking_mood"] = waking_mood
    stats_dict["goal_today"] = goal_today

elif morning_or_evening == "e": # evening input

    
    if string_date in date_dict:
        if "sleep_hours" in date_dict[string_date] and "gym_today" in date_dict[string_date] and "waking_mood" in date_dict[string_date] and "goal_today" in date_dict[string_date] and "streak" in date_dict[string_date]:
            sleep_hours = date_dict[string_date]["sleep_hours"]
            gym_today = date_dict[string_date]["gym_today"]
            waking_mood = date_dict[string_date]["waking_mood"]
            goal_today = date_dict[string_date]["goal_today"]
            stats_dict["streak"] = date_dict[string_date]["streak"]

    print("--- EVENING SYSTEM CHECK ---")

    # gathering evening inputs
    win_today = input("What is one win from today? ")
    hours_worked = numerical_check("How many hours did you work today? ")
    mood_evening = input("How do you feel after today? ")
    goal_achieved = yes_or_no("Was today's goal achieved? (y/n) ")
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

    stats_dict["win_today"] = win_today
    stats_dict["hours_worked"] = hours_worked
    stats_dict["mood_evening"] = mood_evening
    stats_dict["goal_achieved"] = goal_achieved
    stats_dict["morning_message"] = message_for_morning

# check whether to increment or reset streak for today
if string_date not in date_dict:
    streak_check(date_dict)
else:
    stats_dict["streak"] = date_dict[string_date].get("streak", 0)

date_dict[string_date] = stats_dict

# dump dictionary object to json text file
with open("daily_data.json", "w") as file:
    json.dump(date_dict, file)

# weekly summary feature where program summarizes past seven or less entries for user
# weekly not in the sense of the past 7 calendar days but insertion order into list because app only appends today's entry
n = 7
weekly_summary = yes_or_no(f"Would you like to see a summary of the past {n} entries inputted so far? (y/n): ")
if weekly_summary == "y":
    if len(date_dict) < n:
        summarize(date_dict)
    else:
        subset_date_dict = dict(list(date_dict.items())[-n:])
        summarize(subset_date_dict)
else:
    pass



# original text file storage code
# use JSON instead because we can cleanly store + extract data instead of having to parse data from a raw text file
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


