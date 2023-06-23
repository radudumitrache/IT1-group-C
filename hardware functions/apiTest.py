import requests
from pprint import pprint

# List of endpoints
# http://34.91.50.27/teachers/
# http://34.91.50.27/teacher-bookings/
# http://34.91.50.27/students/
# http://34.91.50.27/student-bookings/
# http://34.91.50.27/rooms/
# http://34.91.50.27/student-lectures/
# http://34.91.50.27/lectures/
# http://34.91.50.27/lecture-types/

lecture_types = {"werkcollege", "workshop", "atelier", "hoorcollege", "tutorial", "lecture", "plenary", "plenair",
                 "process" "groepswerk", "professional skills", "assessments", "theorie", "proces", "studiemiddag",
                 "ontwikkeloverleg", "dutch", "reservation"}


def get_lecture_type(lecture_name: str):
    lecture_name = lecture_name.lower()
    for lecture_type in lecture_types:
        if lecture_type in lecture_name:
            return lecture_type

    return "none"

schedule = requests.get("http://34.91.50.27/student-lectures/").json()
teachers = requests.get("http://34.91.50.27/teachers/").json()
rooms = requests.get("http://34.91.50.27/rooms/").json()
lectures = requests.get("http://34.91.50.27/lectures/").json()

print(schedule)
print(teachers)
print(rooms)
print(lectures)
print()

for event in schedule:
    print(event)

    for teacher in teachers:
        if teacher["teacher_number"] == event["teacher_number"]:
            print(teacher["first_name"] + " " + teacher["last_name"])

    for lecture in lectures:
        if lecture["lecture_id"] == event["lecture_id"]:
            print(lecture["lecture_name"])
            print(get_lecture_type(lecture["lecture_name"]))

