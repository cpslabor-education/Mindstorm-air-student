"""robcontroller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

# Variables


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

# Startup


# Main loop:
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    
    
    
    pass

# Enter here exit cleanup code.
