import machine
import utime
import json

from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

# Initialize I2C
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
# Initialize LCD
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


# Pin assignments for the first RGB LED ROOM 1.036
RED_PIN_1 = 2  # 4
GREEN_PIN_1 = 3  # 5
BLUE_PIN_1 = 4  # 6

# Pin assignments for the second RGB LED ROOM 1.035
RED_PIN_2 = 5  # 7
GREEN_PIN_2 = 6  # 9
BLUE_PIN_2 = 7  # 10

# Pin assignments for the third RGB LED ROOM 1.012
RED_PIN_3 = 8  # 11
GREEN_PIN_3 = 9  # 12
BLUE_PIN_3 = 10  # 14

# Pin assignments for the fourth RGB LED ROOM 1.007
RED_PIN_4 = 11  # 15
GREEN_PIN_4 = 12  # 16
BLUE_PIN_4 = 13  # 17

# Pin assignments for the fifth RGB LED ROOM 1.008
RED_PIN_5 = 14  # 19
GREEN_PIN_5 = 15  # 20
BLUE_PIN_5 = 16  # 21

# Pin assignments for the sixth RGB LED ROOM 1.015
RED_PIN_6 = 28  # 34
GREEN_PIN_6 = 27  # 32
BLUE_PIN_6 = 26  # 31

# Pin assignments for the seventh RGB LED ROOM 1.016
RED_PIN_7 = 22  # 29
GREEN_PIN_7 = 21  # 27
BLUE_PIN_7 = 20  # 26

# Pin assignments for the eight RGB LED  K 5.01
RED_PIN_8 = 19  # 25
GREEN_PIN_8 = 18  # 24
BLUE_PIN_8 = 17  # 22

# Pin assignments for the ninth RGB LED
#RED_PIN_9 =   # 
#GREEN_PIN_9 =   # 
#BLUE_PIN_9 =   # 

# Set up pin modes as outputs
red_pin_1 = machine.Pin(RED_PIN_1, machine.Pin.OUT)
green_pin_1 = machine.Pin(GREEN_PIN_1, machine.Pin.OUT)
blue_pin_1 = machine.Pin(BLUE_PIN_1, machine.Pin.OUT)

red_pin_2 = machine.Pin(RED_PIN_2, machine.Pin.OUT)
green_pin_2 = machine.Pin(GREEN_PIN_2, machine.Pin.OUT)
blue_pin_2 = machine.Pin(BLUE_PIN_2, machine.Pin.OUT)

red_pin_3 = machine.Pin(RED_PIN_3, machine.Pin.OUT)
green_pin_3 = machine.Pin(GREEN_PIN_3, machine.Pin.OUT)
blue_pin_3 = machine.Pin(BLUE_PIN_3, machine.Pin.OUT)

red_pin_4 = machine.Pin(RED_PIN_4, machine.Pin.OUT)
green_pin_4 = machine.Pin(GREEN_PIN_4, machine.Pin.OUT)
blue_pin_4 = machine.Pin(BLUE_PIN_4, machine.Pin.OUT)

red_pin_5 = machine.Pin(RED_PIN_5, machine.Pin.OUT)
green_pin_5 = machine.Pin(GREEN_PIN_5, machine.Pin.OUT)
blue_pin_5 = machine.Pin(BLUE_PIN_5, machine.Pin.OUT)

red_pin_6 = machine.Pin(RED_PIN_6, machine.Pin.OUT)
green_pin_6 = machine.Pin(GREEN_PIN_6, machine.Pin.OUT)
blue_pin_6 = machine.Pin(BLUE_PIN_6, machine.Pin.OUT)

red_pin_7 = machine.Pin(RED_PIN_7, machine.Pin.OUT)
green_pin_7 = machine.Pin(GREEN_PIN_7, machine.Pin.OUT)
blue_pin_7 = machine.Pin(BLUE_PIN_7, machine.Pin.OUT)

red_pin_8 = machine.Pin(RED_PIN_8, machine.Pin.OUT)
green_pin_8 = machine.Pin(GREEN_PIN_8, machine.Pin.OUT)
blue_pin_8 = machine.Pin(BLUE_PIN_8, machine.Pin.OUT)




#function to set the RGB values
def set_rgb_room_1_007(red, green, blue):
    red_pin_4.value(red)
    green_pin_4.value(green)
    blue_pin_4.value(blue)

def set_rgb_room_1_008(red, green, blue):
    red_pin_5.value(red)
    green_pin_5.value(green)
    blue_pin_5.value(blue)

def set_rgb_room_1_012(red, green, blue):
    red_pin_3.value(red)
    green_pin_3.value(green)
    blue_pin_3.value(blue)

def set_rgb_room_1_015(red, green, blue):
    red_pin_6.value(red)
    green_pin_6.value(green)
    blue_pin_6.value(blue)

def set_rgb_room_1_016(red, green, blue):
    red_pin_7.value(red)
    green_pin_7.value(green)
    blue_pin_7.value(blue)

def set_rgb_room_1_035(red, green, blue):
    red_pin_2.value(red)
    green_pin_2.value(green)
    blue_pin_2.value(blue)

def set_rgb_room_1_040(red, green, blue):
    red_pin_1.value(red)
    green_pin_1.value(green)
    blue_pin_1.value(blue)

def set_rgb_room_1_028(red, green, blue):
    red_pin_8.value(red)
    green_pin_8.value(green)
    blue_pin_8.value(blue)


#Color Declaration
RED = (0, 255, 255)
GREEN = (255, 0, 255)
BLUE = (255, 255, 0)
YELLOW = (0, 0, 255)
PINK = (0, 190, 100)
OFF = (255, 255, 255)
PURPLE= (150,255, 150)
ORANGE = (0, 165, 255)


set_rgb_room_1_035(*RED)

set_rgb_room_1_012(*GREEN)

set_rgb_room_1_007(*YELLOW)

set_rgb_room_1_008(*PINK)

set_rgb_room_1_015(*BLUE)

set_rgb_room_1_016(*PINK)


#LCD FUNCTIONS LCD FUNCTIONS
name = "Dumitrache, Alex Timothy"
# Names for each row
row2_name = "Maksym Maksym"
row3_name = "Vlad Radu"
row4_name = "Nefeli Nefeli"
availableSpace = 20

def displayText(text: str, screenLength: int):
    if len(text) > screenLength:
        index = 0
        while index + screenLength <= len(text):
            charIndex = 0 + index
            stringBuild = ""

            while (charIndex < screenLength + index) & (charIndex < len(text)):
                stringBuild = stringBuild + text[charIndex]
                charIndex += 1

            lcd.clear()  # Clear the LCD screen
            lcd.putstr(stringBuild)  # Display the text on LCD
            index += 1
            utime.sleep(0.5)

        utime.sleep(1)  # Delay, modify as necessary

    else:
        lcd.clear()
        lcd.putstr(text)


def get_lecture_type(lecture_name: str):
    lecture_name = lecture_name.lower()
    for lecture_type in lecture_types:
        if lecture_type in lecture_name:
            return lecture_type

    return "none"


def get_room_number(location: str):
    if len(location) > 1:
        rooms = list()
        for element in location.split():
            if '-' in element:
                rooms.append(element.split("-")[1])
        return rooms
    else:
        return


def change_led(lecture_type: str, room: str):

    if room == "1.007":
        room_led = set_rgb_room_1_007
    elif room == "1.008":
        room_led = set_rgb_room_1_008
    elif room == "1.012":
        room_led = set_rgb_room_1_012
    elif room == "1.015":
        room_led = set_rgb_room_1_015
    elif room == "1.016":
        room_led = set_rgb_room_1_016
    elif room == "1.035":
        room_led = set_rgb_room_1_035
    elif room == "1.040":
        room_led = set_rgb_room_1_040
    elif room == "1.028":
        room_led = set_rgb_room_1_028
    else:
        return

    if lecture_type == "atelier":
        room_led(*RED)
    elif (lecture_type == "workshop") | (lecture_type == "werkcollege"):
        room_led(*PURPLE)
    elif (lecture_type == "tutorial") | (lecture_type == "hoorcollege"):
        room_led(*YELLOW)
    elif (lecture_type == "plenary") | (lecture_type == "plenair"):
        room_led(*BLUE)
    elif (lecture_type == "process") | (lecture_type == "proces"):
        room_led(*ORANGE)
    elif lecture_type == "reservation":
        room_led(*PINK)
    else:
        room_led(*GREEN)


def display_teachers(teachers: list, room: str):
    for teacher in teachers:
        displayText(teacher, 20)


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


lecture_types = {"werkcollege", "workshop", "atelier", "hoorcollege", "tutorial", "lecture", "plenary", "plenair",
                 "process" "groepswerk", "professional skills", "assessments", "theorie", "proces", "studiemiddag",
                 "ontwikkeloverleg", "dutch", "reservation"}

f = open("jsonText.txt", "r")
dictionary = json.loads(f.read())

for i in range(1):
    now = utime.localtime()

    year, month, day, hour, minute, sec, weekday, yearday = (now)
    current_time = "{:02d}:{:02d}:{:02d}".format(hour, minute, sec)
    current_date = "{:02d}/{:02d}/{}".format(day, month, year)
    
    print("Date: " + current_date)
    print("Time: " + current_time)

    for event in dictionary:
        if current_date == dictionary[event]["date"]:
            description = dictionary[event]['description']
            if (dictionary[event]['start'] <= current_time) & (current_time < dictionary[event]['end']):

                lecture_type = description["lecture type"]
                list_of_teachers = description["list of teachers"]
                rooms = get_room_number(dictionary[event]["location"])

                print("Current lesson: " + lecture_type)
                print("Teachers: ")
                print(list_of_teachers)
                print("Rooms: ")
                print(rooms)
                for room in rooms:
                    if room is not None:
                        change_led(get_lecture_type(lecture_type), room)

                if len(rooms) == 1:
                    display_teachers(list_of_teachers, rooms[0])
                    


