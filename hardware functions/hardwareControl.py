import machine
from machine import Pin, PWM
import utime
import json

import network
import urequests
from time import sleep

from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR_1 = 0x27
I2C_ADDR_2 = 0x23
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd1 = I2cLcd(i2c, I2C_ADDR_1, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd2 = I2cLcd(i2c, I2C_ADDR_2, I2C_NUM_ROWS, I2C_NUM_COLS)



#Slice 0 - RGB LED ROOM 1.036:
RED_PIN_1 = 16
GREEN_PIN_1 = 2
BLUE_PIN_1 = 4

#Slice 1 - RGB LED ROOM 1.035:
RED_PIN_2 = 6
GREEN_PIN_2 = 8
BLUE_PIN_2 = 10

#Slice 2 - RGB LED ROOM 1.012:
RED_PIN_3 = 12
GREEN_PIN_3 = 14
BLUE_PIN_3 = 17

#Slice 3 - RGB LED ROOM 1.007:
RED_PIN_4 = 3
GREEN_PIN_4 = 5
BLUE_PIN_4 = 7

#Slice 4 - RGB LED ROOM 1.008:
RED_PIN_5 = 9
GREEN_PIN_5 = 11
BLUE_PIN_5 = 13

#Slice 5 - RGB LED ROOM 1.015:
RED_PIN_6 = 21
GREEN_PIN_6 = 22
BLUE_PIN_6 = 26

#Slice 6 - RGB LED ROOM 1.016:
RED_PIN_7 = 18
GREEN_PIN_7 = 19
BLUE_PIN_7 = 20

#Slice 7 - RGB LED K 5.01:
RED_PIN_8 = 15
GREEN_PIN_8 = 27
BLUE_PIN_8 = 28


RED_PIN_1 = PWM(Pin(RED_PIN_1))
GREEN_PIN_1 = PWM(Pin(GREEN_PIN_1))
BLUE_PIN_1 = PWM(Pin(BLUE_PIN_1))
RED_PIN_1.freq(1000)
GREEN_PIN_1.freq(1000)
BLUE_PIN_1.freq(1000)
RED_PIN_1.duty_u16(0)
GREEN_PIN_1.duty_u16(0)
BLUE_PIN_1.duty_u16(0)

RED_PIN_2 = PWM(Pin(RED_PIN_2))
GREEN_PIN_2 = PWM(Pin(GREEN_PIN_2))
BLUE_PIN_2 = PWM(Pin(BLUE_PIN_2))
RED_PIN_2.freq(1000)
GREEN_PIN_2.freq(1000)
BLUE_PIN_1.freq(1000)
RED_PIN_2.duty_u16(0)
GREEN_PIN_2.duty_u16(0)
BLUE_PIN_1.duty_u16(0)

RED_PIN_3 = PWM(Pin(RED_PIN_3))
GREEN_PIN_3 = PWM(Pin(GREEN_PIN_3))
BLUE_PIN_3 = PWM(Pin(BLUE_PIN_3))
RED_PIN_3.freq(1000)
GREEN_PIN_3.freq(1000)
BLUE_PIN_3.freq(1000)
RED_PIN_3.duty_u16(0)
GREEN_PIN_3.duty_u16(0)
BLUE_PIN_3.duty_u16(0)

RED_PIN_4 = PWM(Pin(RED_PIN_4))
GREEN_PIN_4 = PWM(Pin(GREEN_PIN_4))
BLUE_PIN_4 = PWM(Pin(BLUE_PIN_4))
RED_PIN_4.freq(1000)
GREEN_PIN_4.freq(1000)
BLUE_PIN_4.freq(1000)
RED_PIN_4.duty_u16(0)
GREEN_PIN_4.duty_u16(0)
BLUE_PIN_4.duty_u16(0)

RED_PIN_5 = PWM(Pin(RED_PIN_5))
GREEN_PIN_5 = PWM(Pin(GREEN_PIN_5))
BLUE_PIN_5 = PWM(Pin(BLUE_PIN_5))
RED_PIN_5.freq(1000)
GREEN_PIN_5.freq(1000)
BLUE_PIN_5.freq(1000)
RED_PIN_5.duty_u16(0)
GREEN_PIN_5.duty_u16(0)
BLUE_PIN_5.duty_u16(0)


# Define pin numbers for RGB LED 1.015
RED_PIN_6 = machine.Pin(21, machine.Pin.OUT)
GREEN_PIN_6 = machine.Pin(22, machine.Pin.OUT)
BLUE_PIN_6 = machine.Pin(26, machine.Pin.OUT)

# Define pin numbers for RGB LED 1.016
RED_PIN_7 = machine.Pin(18, machine.Pin.OUT)
GREEN_PIN_7 = machine.Pin(19, machine.Pin.OUT)
BLUE_PIN_7 = machine.Pin(20, machine.Pin.OUT)

# Define pin numbers for RGB LED K.1.05
RED_PIN_8 = machine.Pin(15, machine.Pin.OUT)
GREEN_PIN_8 = machine.Pin(27, machine.Pin.OUT)
BLUE_PIN_8 = machine.Pin(28, machine.Pin.OUT)



def set_rgb_room_1_036(color):
    RED_PIN_1.duty_u16(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_1.duty_u16(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_1.duty_u16(color[2] * 257)  # Scale from 0-255 to 0-65535

def set_rgb_room_1_035(color):
    RED_PIN_2.duty_u16(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_2.duty_u16(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_2.duty_u16(color[2] * 257)  # Scale from 0-255 to 0-65535

def set_rgb_room_1_012(color):
    RED_PIN_3.duty_u16(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_3.duty_u16(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_3.duty_u16(color[2] * 257)  # Scale from 0-255 to 0-65535

def set_rgb_room_1_007(color):
    RED_PIN_4.duty_u16(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_4.duty_u16(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_4.duty_u16(color[2] * 257)  # Scale from 0-255 to 0-65535

def set_rgb_room_1_008(color):
    RED_PIN_5.duty_u16(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_5.duty_u16(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_5.duty_u16(color[2] * 257)  # Scale from 0-255 to 0-65535

def set_rgb_room_1_015(color):
    RED_PIN_6.value(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_6.value(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_6.value(color[2] * 257)  # Scale from 0-255 to 0-65535

def set_rgb_room_1_016(color):
    RED_PIN_7.value(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_7.value(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_7.value(color[2] * 257)  # Scale from 0-255 to 0-65535

def set_rgb_room_K_5_01(color):
    RED_PIN_8.value(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_8.value(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_8.value(color[2] * 257)  # Scale from 0-255 to 0-65535
    
#def set_rgb_room_1_015(red, green, blue):
#    RED_PIN_6.value(red)
#    GREEN_PIN_6.value(green)
#    BLUE_PIN_6.value(blue)

#def set_rgb_room_1_016(red, green, blue):
#    RED_PIN_7.value(red)
#    GREEN_PIN_7.value(green)
 #   BLUE_PIN_7.value(blue)

#def set_rgb_room_K_5_01(red, green, blue):
#    RED_PIN_8.value(red)
#    GREEN_PIN_8.value(green)
#    BLUE_PIN_8.value(blue)

# Color Declaration
RED = (0, 255, 255)
GREEN = (255, 0, 255)
BLUE = (255, 255, 0)
YELLOW = (0, 150, 255)
PINK = (0, 200, 100)
OFF = (255, 255, 255)
PURPLE = (0, 255, 0)
ORANGE = (0, 220, 255)
WHITE = (0, 0, 0)

set_rgb_room_1_036(OFF)

set_rgb_room_1_035(OFF)

set_rgb_room_1_012(OFF)

set_rgb_room_1_007(OFF)

set_rgb_room_1_008(OFF)

set_rgb_room_1_015(OFF)

set_rgb_room_1_016(OFF)

set_rgb_room_K_5_01(OFF)

while True:

    set_rgb_room_1_008(RED)
    utime.sleep(1)
    set_rgb_room_1_008(BLUE)
    utime.sleep(1)
    set_rgb_room_1_008(GREEN)
    utime.sleep(1)
    set_rgb_room_1_008(PINK)
    utime.sleep(1)    
    set_rgb_room_1_008(PURPLE)
    utime.sleep(1)
    set_rgb_room_1_008(ORANGE)
    utime.sleep(1)
    set_rgb_room_1_008(YELLOW)
    utime.sleep(1)
    set_rgb_room_1_008(WHITE)
    utime.sleep(1)

    set_rgb_room_K_5_01(RED)
    utime.sleep(1)
    set_rgb_room_K_5_01(BLUE)
    utime.sleep(1)
    set_rgb_room_K_5_01(GREEN)
    utime.sleep(1)
    set_rgb_room_K_5_01(PINK)
    utime.sleep(1)    
    set_rgb_room_K_5_01(PURPLE)
    utime.sleep(1)
    set_rgb_room_K_5_01(ORANGE)
    utime.sleep(1)
    set_rgb_room_K_5_01(YELLOW)
    utime.sleep(1)
    set_rgb_room_K_5_01(WHITE)
    utime.sleep(1)



    set_rgb_room_1_007(RED)
    utime.sleep(1)
    set_rgb_room_1_007(BLUE)
    utime.sleep(1)
    set_rgb_room_1_007(GREEN)
    utime.sleep(1)
    set_rgb_room_1_007(PINK)
    utime.sleep(1)    
    set_rgb_room_1_007(PURPLE)
    utime.sleep(1)
    set_rgb_room_1_007(ORANGE)
    utime.sleep(1)
    set_rgb_room_1_007(YELLOW)
    utime.sleep(1)


    set_rgb_room_1_012(RED)
    utime.sleep(1)
    set_rgb_room_1_012(BLUE)
    utime.sleep(1)
    set_rgb_room_1_012(GREEN)
    utime.sleep(1)
    set_rgb_room_1_012(PINK)
    utime.sleep(1)    
    set_rgb_room_1_012(PURPLE)
    utime.sleep(1)
    set_rgb_room_1_012(ORANGE)
    utime.sleep(1)
    set_rgb_room_1_012(YELLOW)
    utime.sleep(1)
    

    set_rgb_room_1_015(RED)
    utime.sleep(1)
    set_rgb_room_1_015(BLUE)
    utime.sleep(1)
    set_rgb_room_1_015(GREEN)
    utime.sleep(1)
    set_rgb_room_1_015(PINK)
    utime.sleep(1)    
    set_rgb_room_1_015(PURPLE)
    utime.sleep(1)
    set_rgb_room_1_015(ORANGE)
    utime.sleep(1)
    set_rgb_room_1_015(YELLOW)
    utime.sleep(1)
    
    set_rgb_room_1_016(RED)
    utime.sleep(1)
    set_rgb_room_1_016(BLUE)
    utime.sleep(1)
    set_rgb_room_1_016(GREEN)
    utime.sleep(1)
    set_rgb_room_1_016(PINK)
    utime.sleep(1)    
    set_rgb_room_1_016(PURPLE)
    utime.sleep(1)
    set_rgb_room_1_016(ORANGE)
    utime.sleep(1)
    set_rgb_room_1_016(YELLOW)
    utime.sleep(1)    

    set_rgb_room_1_035(RED)
    utime.sleep(1)
    set_rgb_room_1_035(BLUE)
    utime.sleep(1)
    set_rgb_room_1_035(GREEN)
    utime.sleep(1)
    set_rgb_room_1_035(PINK)
    utime.sleep(1)    
    set_rgb_room_1_035(PURPLE)
    utime.sleep(1)
    set_rgb_room_1_035(ORANGE)
    utime.sleep(1)
    set_rgb_room_1_035(YELLOW)
    utime.sleep(5) 

    set_rgb_room_1_036(RED)
    utime.sleep(1)
    set_rgb_room_1_036(BLUE)
    utime.sleep(1)
    set_rgb_room_1_036(GREEN)
    utime.sleep(1)
    set_rgb_room_1_036(PINK)
    utime.sleep(1)    
    set_rgb_room_1_036(PURPLE)
    utime.sleep(1)
    set_rgb_room_1_036(ORANGE)
    utime.sleep(1)
    set_rgb_room_1_036(YELLOW)
    utime.sleep(5) 







# LCD FUNCTIONS LCD FUNCTIONS
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

            lcd1.clear()  # Clear the LCD screen
            lcd1.putstr(stringBuild)  # Display the text on LCD
            index += 1
            utime.sleep(0.5)

        utime.sleep(1)  # Delay, modify as necessary

    else:
        lcd1.clear()
        lcd1.putstr(text)


def displayText2(text: str, screenLength: int):
    if len(text) > screenLength:
        index = 0
        while index + screenLength <= len(text):
            charIndex = 0 + index
            stringBuild = ""

            while (charIndex < screenLength + index) & (charIndex < len(text)):
                stringBuild = stringBuild + text[charIndex]
                charIndex += 1

            lcd2.clear()  # Clear the LCD screen
            lcd2.putstr(stringBuild)  # Display the text on LCD
            index += 1
            utime.sleep(0.5)

        utime.sleep(1)  # Delay, modify as necessary

    else:
        lcd2.clear()
        lcd2.putstr(text)


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
    print(room)
    print(lecture_type)
    print("")

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
    lcd1.move_to(3, 0)
    lcd1.putstr("ROOM " + room)

    if (len(teachers) < 3):
        for i in range(len(teachers)):
            lcd1.move_to(0, i + 1)
            lcd1.putstr(teachers[i])
    else:
        lcd1.move_to(0, 1)
        lcd1.putstr(teachers[0])
        lcd1.move_to(0, 2)
        lcd1.putstr(teachers[1])
        lcd1.move_to(0, 3)
        lcd1.putstr(teachers[2])


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


ssid = "samba1"

# Set up the Wi-Fi connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid)

while wifi.isconnected() == False:
    print('Waiting for connection...')
    sleep(1)

ip = wifi.ifconfig()
print(f'Connected on {ip}')

print('Connected. IP address:', wifi.ifconfig()[0])

# wait for API to update
# when API updates, get the latest data
# first key of the JSON might be room number


lecture_types = {"werkcollege", "workshop", "atelier", "hoorcollege", "tutorial", "lecture", "plenary", "plenair",
                 "process" "groepswerk", "professional skills", "assessments", "theorie", "proces", "studiemiddag",
                 "ontwikkeloverleg", "dutch", "reservation"}

# replace with API GET request
f = open("jsonText.txt", "r")
dictionary = json.loads(f.read())

nextMinute = 0
while True:
    now = utime.localtime()

    year, month, day, hour, minute, sec, weekday, yearday = now
    current_time = "{:02d}:{:02d}:{:02d}".format(hour, minute, sec)
    current_date = "{}-{:02d}-{:02d}".format(year, month, day)

    print("Date: " + current_date)
    print("Time: " + current_time)

    nextMinute = minute + 1
    # replace with API GET request
    f = open("jsonText.txt", "r")
    dictionary = json.loads(f.read())

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

    # loop through every room, store room in a list, store list of teachers in a parallel list
    # below loop through both while
    while nextMinute >= minute:
        
        now = utime.localtime()
        year, month, day, hour, minute, sec, weekday, yearday = now

        for room in rooms:
            display_teachers(list_of_teachers, room)

        utime.sleep(1)
