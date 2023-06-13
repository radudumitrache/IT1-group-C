from machine import Pin,PWM
from time import sleep


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





RED_PIN_1=PWM(Pin(RED_PIN_1))
GREEN_PIN_1=PWM(Pin(GREEN_PIN_1))
BLUE_PIN_1=PWM(Pin(BLUE_PIN_1))
RED_PIN_1.freq(1000)
GREEN_PIN_1.freq(1000)
BLUE_PIN_1.freq(1000)
RED_PIN_1.duty_u16(0)
GREEN_PIN_1.duty_u16(0)
BLUE_PIN_1.duty_u16(0)


RED_PIN_2=PWM(Pin(RED_PIN_2))
GREEN_PIN_2=PWM(Pin(GREEN_PIN_2))
BLUE_PIN_2=PWM(Pin(BLUE_PIN_2))
RED_PIN_2.freq(1000)
GREEN_PIN_2.freq(1000)
BLUE_PIN_1.freq(1000)
RED_PIN_2.duty_u16(0)
GREEN_PIN_2.duty_u16(0)
BLUE_PIN_1.duty_u16(0)


RED_PIN_3=PWM(Pin(RED_PIN_3))
GREEN_PIN_3=PWM(Pin(GREEN_PIN_3))
BLUE_PIN_3=PWM(Pin(BLUE_PIN_3))
RED_PIN_3.freq(1000)
GREEN_PIN_3.freq(1000)
BLUE_PIN_3.freq(1000)
RED_PIN_3.duty_u16(0)
GREEN_PIN_3.duty_u16(0)
BLUE_PIN_3.duty_u16(0)


RED_PIN_4=PWM(Pin(RED_PIN_4))
GREEN_PIN_4=PWM(Pin(GREEN_PIN_4))
BLUE_PIN_4=PWM(Pin(BLUE_PIN_4))
RED_PIN_4.freq(1000)
GREEN_PIN_4.freq(1000)
BLUE_PIN_4.freq(1000)
RED_PIN_4.duty_u16(0)
GREEN_PIN_4.duty_u16(0)
BLUE_PIN_4.duty_u16(0)


RED_PIN_5=PWM(Pin(RED_PIN_5))
GREEN_PIN_5=PWM(Pin(GREEN_PIN_5))
BLUE_PIN_5=PWM(Pin(BLUE_PIN_5))
RED_PIN_5.freq(1000)
GREEN_PIN_5.freq(1000)
BLUE_PIN_5.freq(1000)
RED_PIN_5.duty_u16(0)
GREEN_PIN_5.duty_u16(0)
BLUE_PIN_5.duty_u16(0)


RED_PIN_6=PWM(Pin(RED_PIN_6))
GREEN_PIN_6=PWM(Pin(GREEN_PIN_6))
BLUE_PIN_6=PWM(Pin(BLUE_PIN_6))
RED_PIN_6.freq(1000)
GREEN_PIN_6.freq(1000)
BLUE_PIN_6.freq(1000)
RED_PIN_6.duty_u16(0)
GREEN_PIN_6.duty_u16(0)
BLUE_PIN_6.duty_u16(0)


RED_PIN_7=PWM(Pin(RED_PIN_7))
GREEN_PIN_7=PWM(Pin(GREEN_PIN_7))
BLUE_PIN_7=PWM(Pin(BLUE_PIN_7))
RED_PIN_7.freq(1000)
GREEN_PIN_7.freq(1000)
BLUE_PIN_7.freq(1000)
RED_PIN_7.duty_u16(0)
GREEN_PIN_7.duty_u16(0)
BLUE_PIN_7.duty_u16(0)

RED_PIN_8=PWM(Pin(RED_PIN_8))
GREEN_PIN_8=PWM(Pin(GREEN_PIN_8))
BLUE_PIN_8=PWM(Pin(BLUE_PIN_8))
RED_PIN_8.freq(1000)
GREEN_PIN_8.freq(1000)
BLUE_PIN_8.freq(1000)
RED_PIN_8.duty_u16(0)
GREEN_PIN_8.duty_u16(0)
BLUE_PIN_8.duty_u16(0)


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
    RED_PIN_6.duty_u16(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_6.duty_u16(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_6.duty_u16(color[2] * 257)  # Scale from 0-255 to 0-65535


def set_rgb_room_1_016(color):
    RED_PIN_7.duty_u16(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_7.duty_u16(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_7.duty_u16(color[2] * 257)  # Scale from 0-255 to 0-65535


def set_rgb_room_K_5_01(color):
    RED_PIN_8.duty_u16(color[0] * 257)  # Scale from 0-255 to 0-65535
    GREEN_PIN_8.duty_u16(color[1] * 257)  # Scale from 0-255 to 0-65535
    BLUE_PIN_8.duty_u16(color[2] * 257)  # Scale from 0-255 to 0-65535

# Color Declaration
RED = (0, 255, 255)
GREEN = (255, 0, 255)
BLUE = (255, 255, 0)
YELLOW = (0, 0, 255)
PINK = (0, 190, 100)
OFF = (255, 255, 255)
PURPLE = (20, 223, 15)
ORANGE = (0, 100, 255)


set_rgb_room_1_015(BLUE)
sleep(15)
set_rgb_room_1_016(YELLOW)
sleep(15)

set_rgb_room_K_5_01(ORANGE)
sleep(15)