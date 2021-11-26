"""robcontroller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
import math

from controller import Robot
from controller import Keyboard

robot = Robot()
keyboard1 = Keyboard()
keyboard2 = Keyboard()

timestep = int(robot.getBasicTimeStep())

# Variables
max_velocity = robot.getDevice('wheel_r1').getMaxVelocity()
forward_speed = 1 * max_velocity
turn_speed = 0.7 * max_velocity


# Setup wheels
wheel_r1 = robot.getDevice('wheel_r1')
wheel_r2 = robot.getDevice('wheel_r2')
wheel_r3 = robot.getDevice('wheel_r3')
wheel_l1 = robot.getDevice('wheel_l1')
wheel_l2 = robot.getDevice('wheel_l2')
wheel_l3 = robot.getDevice('wheel_l3')
    
right_wheels = [wheel_r1, wheel_r2, wheel_r3]
left_wheels = [wheel_l1, wheel_l2, wheel_l3]
    
for wheel in right_wheels:
    wheel.setPosition(float('inf'))
    wheel.setVelocity(0.0)
for wheel in left_wheels:
    wheel.setPosition(float('inf'))
    wheel.setVelocity(0.0)


# Functions

def SetRightMotor(velocity: float):
    for wheel in right_wheels:
        wheel.setVelocity(velocity)

def SetLeftMotor(velocity: float):
    for wheel in left_wheels:
        wheel.setVelocity(velocity)

def SetMotors(v_right: float, v_left: float):
    SetRightMotor(v_right)
    SetLeftMotor(v_left)

def GetVelocity_Keyboard():
    velocities = [0,0]
    key1 = keyboard1.getKey()
    key2 = keyboard2.getKey()
    # Get forward input
    if (key1 == ord('W') or key2 == ord('W')):
        velocities = [forward_speed, forward_speed]
    elif (key1 == ord('S') or key2 == ord('S')):
        velocities = [-forward_speed, -forward_speed]
    # Get side input
    if (key1 == ord('D') or key2 == ord('D')):
        if velocities == [0,0]:
            velocities = [turn_speed, -turn_speed]
        else:
            velocities[1] = (velocities[1]/forward_speed) * (max_velocity-turn_speed)
    elif (key1 == ord('A') or key2 == ord('A')):
        if velocities == [0,0]:
            velocities = [-turn_speed, turn_speed]
        else:
            velocities[0] = (velocities[0]/forward_speed) * (max_velocity-turn_speed)
    
    return velocities
    
    

# Startup
keyboard1.enable(timestep)
keyboard2.enable(timestep)

# Main loop:
while robot.step(timestep) != -1:
    
    velocities = GetVelocity_Keyboard()
    SetMotors(velocities[0], velocities[1])
    
    pass

# Enter here exit cleanup code.
