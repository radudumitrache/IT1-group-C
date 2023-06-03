from icalendar import *
from pprint import pprint
from datetime import datetime
from time import sleep
from calendarParser import calendar_parse

"""
Todo:
- Separate things into functions
- Determine format for the BIG JSON file
- Change logic so it works with the BIG JSON file
- Get multiple rooms instead of just one
"""


def get_lecture_type(lecture_name: str):
    lecture_name = lecture_name.lower()
    for lecture_type in lecture_types:
        if lecture_name == lecture_type:
            return lecture_name

    return "none"


def get_room(location: str):
    if len(location) > 1:
        rooms = list()
        for element in location.split():
            if '-' in element:
                rooms.append(element.split("-")[1])
        return rooms
    else:
        return


def change_led(lecture_type: str, room: str):
    if lecture_type == "atelier":
        print("Red")
    elif (lecture_type == "workshop") | (lecture_type == "werkcollege"):
        print("Purple")
    elif (lecture_type == "tutorial") | (lecture_type == "hoorcollege"):
        print("Yellow")
    elif (lecture_type == "plenary") | (lecture_type == "plenair"):
        print("Blue")
    elif (lecture_type == "process") | (lecture_type == "proces"):
        print("Orange")
    elif lecture_type == "reservation":
        print("Pink")
    else:
        print("Green")


def overlap_check(schedule: str):

    previous_event = None
    current_event = None

    for event in schedule:

        if previous_event is None:
            previous_event = event
            continue

        current_event = event

        if dictionary[current_event]["date"] == dictionary[previous_event]["date"]:
            if dictionary[current_event]["start"] > dictionary[previous_event]["end"]:
                if get_lecture_type(dictionary[current_event]["description"]["lecture_type"]) == "reservation":
                    dictionary.pop([current_event])
                elif get_lecture_type(dictionary[previous_event]["description"]["lecture_type"]) == "reservation":
                    dictionary.pop([previous_event])
                else:
                    dictionary.pop([current_event])

        previous_event = current_event

    return

# wait for API to update
# when API updates, get the latest data
# first key of the JSON might be room number


calendar_file = open('week-22-2023.ics', 'rb')
calendar = Calendar.from_ical(calendar_file.read())

lecture_types = {"werkcollege", "workshop", "atelier", "hoorcollege", "tutorial", "lecture", "plenary", "plenair",
                 "process" "groepswerk", "professional skills", "assessments", "theorie", "proces", "studiemiddag",
                 "ontwikkeloverleg", "dutch", "reservation"}

dictionary = calendar_parse(calendar)

for i in range(1):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    print("Date: " + current_date)
    print("Time: " + current_time)

    for event in dictionary:
        print("Rooms: " + str(get_room(dictionary[event]["location"])))
        if current_date == dictionary[event]["date"]:
            description = dictionary[event]['description']
            if (dictionary[event]['start'] < current_time) & (current_time < dictionary[event]['end']):

                lecture_type = description["lecture type"]
                list_of_teachers = description["list of teachers"]
                rooms = get_room(description["location"])

                print("Current lesson: " + lecture_type)
                print("Teachers: ")
                print(list_of_teachers)
                for room in rooms:
                    if room is not None:
                        change_led(get_lecture_type(lecture_type), room)

    # sleep(60)
