"""!
@file main.py
This file contains code used to operate the ME405 motot 

@details The main script calls the MotorDriver class and EncoderDriver class,
imported as modules, to operate the motor and encoders.
    
@author Nishka Chawla
@author Ronan Shaffer
@date   26-Jan-2022
@copyright (c) Released under GNU Public License
"""

import pyb
import time
import motor_chawla_shaffer
import encoder_chawla_shaffer

## Input pin configuration
inn = pyb.Pin.IN

## Output with push-pull control pin configuration
out = pyb.Pin.OUT_PP

# Define motor pins
## The enable pin for the motor. 
pinEN = pyb.Pin(pyb.Pin.cpu.A10, out)
## Pin variable for channel A of the motor.
pinB4 = pyb.Pin(pyb.Pin.cpu.B4, out)
## Pin variable for channel B of the motor.
pinB5 = pyb.Pin(pyb.Pin.cpu.B5, out)

# Define encoder pins
## Pin variable for channel 1 of the encoder A.
pinB6 = pyb.Pin(pyb.Pin.cpu.B6, out)
## Pin variable for channel 2 of the encoder A.
pinB7 = pyb.Pin(pyb.Pin.cpu.B7, out)
## Pin variable for channel 1 of the encoder B.
pinC6 = pyb.Pin(pyb.Pin.cpu.C6, out)
## Pin variable for channel 2 of the encoder B.
pinC7 = pyb.Pin(pyb.Pin.cpu.C7, out)


if __name__ == '__main__':
    
    ## Instantiation of motor object.
    moe = motor_chawla_shaffer.MotorDriver(pinEN, pinB4, pinB5, 3)
    ## Instantiation of encoder 1 object.
    encoder1 = encoder_chawla_shaffer.EncoderDriver(pinB6, pinB7, 4)
    ## Instantiation of encoder 2 object.
    encoder2 = encoder_chawla_shaffer.EncoderDriver(pinC6, pinC7, 8)
    
    while True:
        
        moe.set_duty_cycle (-142)
        encoder1.update()
        encoder2.update()
        ## Variable storing Encoder 1 position.
        count_A = encoder1.read()
        ## Variable storing Encoder 2 position.
        count_B = encoder2.read()
        
        time.sleep(.2)
        print('ENCA:',count_A,'ENCB:',count_B)
