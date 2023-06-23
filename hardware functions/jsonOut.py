from pprint import pprint
import json
from time import sleep


def get_room_number(location: str):
    if len(location) > 1:
        rooms = list()
        for element in location.split():
            if '-' in element:
                rooms.append(element.split("-")[1])
        return rooms
    else:
        return


f = open("jsonText.txt", "r")
dictionary = json.loads(f.read())
pprint(dictionary)

dictionary = {

    "1.007":["Alex", "Radu"],
    "1.012":["Nefeli", "Vlad"],
    "1.016":["Maksym", "Timothy"]

}

for room in dictionary:
    print(room)
    for teacher in dictionary[room]:
        print(teacher)

    print()
    sleep(5)
