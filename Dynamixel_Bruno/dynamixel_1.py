import PyDynamixel_v2.PyDynamixel_v2 as pd 
from math import pi

BAUDRATE = 100000 
SERIAL = 'COM3'

# Serial setups
serial = pd.DxlComm( SERIAL, BAUDRATE )

# Define the Joints setups
joint1 = pd.Joint(servo_id=1 )
joint2 = pd.Joint(servo_id=28)

# Enable the Joints 
serial.attach_joints( [joint1, joint2] )

# To get the Joint Id
joints = serial.joint_ids

# Enable torque in joints
serial.enable_torques()

# To Write in the Dynamixels
serial.send_angles( {joint1 : 90, joint2 : 60} )
serial.send_angles( {joint1: pi/2, joint2: pi/3}, radian=True )

# To read the dynamixels's angle 
angles = serial.get_angles()
angles = serial.get_angles(radian=True)

# To calculate the ping of all joints attachs
serial.broadcast_ping()

# To calculate the ping of one Joint 
joint1.ping()
