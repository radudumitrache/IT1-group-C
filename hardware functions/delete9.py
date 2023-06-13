from machine import Pin,PWM
from time import sleep
import machine
import utime



# Pin assignments for the first RGB LED ROOM 1.036
RED_PIN_1 = machine.PWM(machine.Pin(2))  # 4
GREEN_PIN_1 = machine.PWM(machine.Pin(3))  # 5
BLUE_PIN_1 = machine.PWM(machine.Pin(4))  # 6
RED_PIN_1.freq(1000)
GREEN_PIN_1.freq(1000)
BLUE_PIN_1.freq(1000)


# Pin assignments for the second RGB LED ROOM 1.035
RED_PIN_2 = machine.PWM(machine.Pin(5))  # 7
GREEN_PIN_2 = machine.PWM(machine.Pin(6))  # 9
BLUE_PIN_2 = machine.PWM(machine.Pin(7))  # 10
RED_PIN_2.freq(1000)
GREEN_PIN_2.freq(1000)
BLUE_PIN_2.freq(1000)

# Pin assignments for the third RGB LED ROOM 1.012
RED_PIN_3 = machine.PWM(machine.Pin(8))  # 11
GREEN_PIN_3 = machine.PWM(machine.Pin(9))  # 12
BLUE_PIN_3 = machine.PWM(machine.Pin(10))  # 14
RED_PIN_3.freq(1000)
GREEN_PIN_3.freq(1000)
BLUE_PIN_3.freq(1000)

# Pin assignments for the fourth RGB LED ROOM 1.007
RED_PIN_4 = machine.PWM(machine.Pin(11))  # 15
GREEN_PIN_4 = machine.PWM(machine.Pin(12))  # 16
BLUE_PIN_4 = machine.PWM(machine.Pin(13))  # 17
RED_PIN_4.freq(1000)
GREEN_PIN_4.freq(1000)
BLUE_PIN_4.freq(1000)

# Pin assignments for the fifth RGB LED ROOM 1.008
RED_PIN_5 = machine.PWM(machine.Pin(14))  # 19
GREEN_PIN_5 = machine.PWM(machine.Pin(15))  # 20
BLUE_PIN_5 = machine.PWM(machine.Pin(16))  # 21
RED_PIN_4.freq(1000)
GREEN_PIN_4.freq(1000)
BLUE_PIN_4.freq(1000)

# Pin assignments for the sixth RGB LED ROOM 1.015
RED_PIN_6 = machine.PWM(machine.Pin(28))  # 34
GREEN_PIN_6 = machine.PWM(machine.Pin(27))  # 32
BLUE_PIN_6 = machine.PWM(machine.Pin(26))  # 31
RED_PIN_4.freq(1000)
GREEN_PIN_4.freq(1000)
BLUE_PIN_4.freq(1000)

# Pin assignments for the seventh RGB LED ROOM 1.016
RED_PIN_7 = machine.PWM(machine.Pin(22))  # 29
GREEN_PIN_7 = machine.PWM(machine.Pin(21))  # 27
BLUE_PIN_7 = machine.PWM(machine.Pin(20))  # 26
RED_PIN_4.freq(1000)
GREEN_PIN_4.freq(1000)
BLUE_PIN_4.freq(1000)

# Pin assignments for the eight RGB LED  K 5.01
RED_PIN_8 = machine.PWM(machine.Pin(19))  # 25
GREEN_PIN_8 = machine.PWM(machine.Pin(18))  # 24
BLUE_PIN_8 = machine.PWM(machine.Pin(17))  # 22
RED_PIN_4.freq(1000)
GREEN_PIN_4.freq(1000)
BLUE_PIN_4.freq(1000)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def color_to_duty(rgb_value):
    rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
    return rgb_value

def set_rgb_room_1_036(red_value,green_value,blue_value):
    RED_PIN_1.duty_u16(color_to_duty(red_value))
    GREEN_PIN_1.duty_u16(color_to_duty(green_value))
    BLUE_PIN_1.duty_u16(color_to_duty(blue_value))
    
def set_rgb_room_1_035(red_value,green_value,blue_value):
    RED_PIN_2.duty_u16(color_to_duty(red_value))
    GREEN_PIN_2.duty_u16(color_to_duty(green_value))
    BLUE_PIN_2.duty_u16(color_to_duty(blue_value))

def set_rgb_room_1_012(red_value,green_value,blue_value):
    RED_PIN_3.duty_u16(color_to_duty(red_value))
    GREEN_PIN_3.duty_u16(color_to_duty(green_value))
    BLUE_PIN_3.duty_u16(color_to_duty(blue_value))
    
def set_rgb_room_1_007(red_value,green_value,blue_value):
    RED_PIN_4.duty_u16(color_to_duty(red_value))
    GREEN_PIN_4.duty_u16(color_to_duty(green_value))
    BLUE_PIN_4.duty_u16(color_to_duty(blue_value))
    
def set_rgb_room_1_008(red_value,green_value,blue_value):
    RED_PIN_5.duty_u16(color_to_duty(red_value))
    GREEN_PIN_5.duty_u16(color_to_duty(green_value))
    BLUE_PIN_5.duty_u16(color_to_duty(blue_value))

def set_rgb_room_1_015(red_value,green_value,blue_value):
    RED_PIN_6.duty_u16(color_to_duty(red_value))
    GREEN_PIN_6.duty_u16(color_to_duty(green_value))
    BLUE_PIN_6.duty_u16(color_to_duty(blue_value))
    
def set_rgb_room_1_016(red_value,green_value,blue_value):
    RED_PIN_7.duty_u16(color_to_duty(red_value))
    GREEN_PIN_7.duty_u16(color_to_duty(green_value))
    BLUE_PIN_7.duty_u16(color_to_duty(blue_value))

def set_rgb_room_K_5_01(red_value,green_value,blue_value):
    RED_PIN_8.duty_u16(color_to_duty(red_value))
    GREEN_PIN_8.duty_u16(color_to_duty(green_value))
    BLUE_PIN_8.duty_u16(color_to_duty(blue_value))


#Color Declaration
RED = (0, 255, 255)
GREEN = (255, 0, 255)
BLUE = (255, 255, 0)
YELLOW = (0, 0, 255)
PINK = (0, 190, 100)
OFF = (255, 255, 255)
PURPLE= (20,223, 15)
ORANGE = (0, 90, 255)


set_rgb_room_1_036(*RED)

set_rgb_room_1_035(*GREEN)

set_rgb_room_1_012(*BLUE)

set_rgb_room_1_007(*YELLOW)

set_rgb_room_1_008(*PINK)

set_rgb_room_1_015(*OFF)

set_rgb_room_1_016(*PURPLE)

set_rgb_room_K_5_01(*ORANGE)
