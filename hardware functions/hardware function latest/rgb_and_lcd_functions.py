import machine
import utime

from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

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
def set_rgb_room_1_036(red, green, blue):
    red_pin_1.value(red)
    green_pin_1.value(green)
    blue_pin_1.value(blue)
    

def set_rgb_room_1_035(red, green, blue):
    red_pin_2.value(red)
    green_pin_2.value(green)
    blue_pin_2.value(blue)
    
def set_rgb_room_1_012(red, green, blue):
    red_pin_3.value(red)
    green_pin_3.value(green)
    blue_pin_3.value(blue)

def set_rgb_room_1_007(red, green, blue):
    red_pin_4.value(red)
    green_pin_4.value(green)
    blue_pin_4.value(blue)

def set_rgb_room_1_008(red, green, blue):
    red_pin_5.value(red)
    green_pin_5.value(green)
    blue_pin_5.value(blue)

def set_rgb_room_1_015(red, green, blue):
    red_pin_6.value(red)
    green_pin_6.value(green)
    blue_pin_6.value(blue)

def set_rgb_room_1_016(red, green, blue):
    red_pin_7.value(red)
    green_pin_7.value(green)
    blue_pin_7.value(blue)


def set_rgb_room_K_5_01(red, green, blue):
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



set_rgb_room_1_036(*BLUE)

set_rgb_room_1_035(*RED)

set_rgb_room_1_012(*GREEN)

set_rgb_room_1_007(*YELLOW)

set_rgb_room_1_008(*PINK)

set_rgb_room_1_015(*BLUE)

set_rgb_room_1_016(*PINK)

set_rgb_room_K_5_01(*ORANGE)


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

# Call the function to display the text
displayText(name, availableSpace)
utime.sleep(1)  # Delay, modify as necessary


# Display names on respective rows
displayText(row2_name, 20)
utime.sleep(1)  # Delay, modify as necessary

displayText(row3_name, 20)
utime.sleep(1)  # Delay, modify as necessary

displayText(row4_name, 11)