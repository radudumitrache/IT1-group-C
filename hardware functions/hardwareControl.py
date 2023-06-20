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

# Init onboard LED
led_onboard = machine.Pin("LED", machine.Pin.OUT)

# Slice 0 - RGB LED ROOM 1.036:
RED_PIN_1 = 16
GREEN_PIN_1 = 2
BLUE_PIN_1 = 4

# Slice 1 - RGB LED ROOM 1.035:
RED_PIN_2 = 6
GREEN_PIN_2 = 8
BLUE_PIN_2 = 10

# Slice 2 - RGB LED ROOM 1.012:
RED_PIN_3 = 12
GREEN_PIN_3 = 14
BLUE_PIN_3 = 17

# Slice 3 - RGB LED ROOM 1.007:
RED_PIN_4 = 3
GREEN_PIN_4 = 5
BLUE_PIN_4 = 7

# Slice 4 - RGB LED ROOM 1.008:
RED_PIN_5 = 9
GREEN_PIN_5 = 11
BLUE_PIN_5 = 13

# Slice 5 - RGB LED ROOM 1.015:
RED_PIN_6 = 21
GREEN_PIN_6 = 22
BLUE_PIN_6 = 26

# Slice 6 - RGB LED ROOM 1.016:
RED_PIN_7 = 18
GREEN_PIN_7 = 19
BLUE_PIN_7 = 20

# Slice 7 - RGB LED K 5.01:
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

def change_led(room: str, availability: bool):
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
    elif room == "1.036":
        room_led = set_rgb_room_1_036
    else:
        return

    if availability:
        room_led(GREEN)
    else:
        room_led(RED)

"""
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
"""

def display_teachers(teachers: list, room: str):
    lcd.move_to(3, 0)
    lcd.putstr("ROOM " + room)

    if (len(teachers) < 3):
        for i in range(len(teachers)):
            lcd.move_to(0, i + 1)
            lcd.putstr(teachers[i])
    else:
        lcd.move_to(0, 1)
        lcd.putstr(teachers[0])
        lcd.move_to(0, 2)
        lcd.putstr(teachers[1])
        lcd.move_to(0, 3)
        lcd.putstr(teachers[2])

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

# Wifi connection
ssid = "Getoffmyproperty"
password = "randomPass9000"

# Set up the Wi-Fi connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

led_onboard.value(0)
while wifi.isconnected() == False:
    print('Waiting for connection...')
    led_onboard.toggle()
    sleep(1)

ip = wifi.ifconfig()
print(f'Connected on {ip}')

print('Connected. IP address:', wifi.ifconfig()[0])
led_onboard.value(1)
sleep(1)

# List of endpoints
# http://34.91.50.27/teachers/
# http://34.91.50.27/teacher-bookings/
# http://34.91.50.27/students/
# http://34.91.50.27/student-bookings/
# http://34.91.50.27/rooms/
# http://34.91.50.27/student-lectures/
# http://34.91.50.27/lectures/
# http://34.91.50.27/lecture-types/


# wait for API to update
# when API updates, get the latest data


lecture_types = {"werkcollege", "workshop", "atelier", "hoorcollege", "tutorial", "lecture", "plenary", "plenair",
                 "process" "groepswerk", "professional skills", "assessments", "theorie", "proces", "studiemiddag",
                 "ontwikkeloverleg", "dutch", "reservation"}

nextMinute = 0
while True:
    now = utime.localtime()

    year, month, day, hour, minute, sec, weekday, yearday = now
    current_time = "{:02d}:{:02d}:{:02d}".format(hour, minute, sec)
    current_date = "{}-{:02d}-{:02d}".format(year, month, day)

    print("Date: " + current_date)
    print("Time: " + current_time)

    nextMinute = minute + 1

    try:
        rooms = urequests.get("http://34.91.50.27/rooms/")
        rooms = rooms.json()
    except:
        print("GET failed")
    else:
        for room in rooms:
            room_number = str(room["room_number"])
            availability = room["availability"]

            room_number = room_number[0] + "." + room_number[1:]
            change_led(room_number, availability)

        counter = 0
        for room in rooms:
            room_number = str(room["room_number"])
            room_number = room_number[0] + "." + room_number[1:]
            availability = room["availability"]

            lcd1.clear()
            lcd1.move_to(3, 0)
            lcd1.putstr("ROOM " + room_number)
            lcd1.move_to(3, 1)

            lcd2.clear()
            lcd2.move_to(3, 0)
            lcd2.putstr("ROOM " + room_number)
            lcd2.move_to(3, 1)

            if availability:
                lcd1.putstr("Available")
                lcd2.putstr("Available")
            else:
                lcd1.putstr("In use")
                lcd2.putstr("In use")

            sleep(5)

