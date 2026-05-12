import pybullet as p

import time

import pybullet_data
p.connect(p.GUI)    

p.configureDebugVisualizer(p.COV_ENABLE_KEYBOARD_SHORTCUTS, 0)


p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -50)   

plane = p.loadURDF("plane.urdf")

#robot = p.loadURDF("cube.urdf",[0,0,1])

robot =p.loadURDF("r2d2.urdf",[0,0,1])

robot2 =p.loadURDF("r2d2.urdf",[1,0,1])

# Enable motors for arm and gripper joints (assuming joint indices: 3=arm, 4=gripper_left, 5=gripper_right)
for joint in [3, 4, 5]:
    p.setJointMotorControl2(robot, joint, p.POSITION_CONTROL, force=1000)
    p.setJointMotorControl2(robot2, joint, p.POSITION_CONTROL, force=1000)

# Control robots with keyboard input
vx = 0
vy = 0
speed = 1
vx2 = 0
vy2 = 0
speed2 = 1

while True:
    p.stepSimulation()
    
    time.sleep(1./241)

    keys = p.getKeyboardEvents()
    
    # Reset velocities to 0 each frame
    vx = 0
    vy = 0
    vx2 = 0
    vy2 = 0
    
    # Control robot2 with W A S D keys
    if ord('w') in keys:
        vy = speed
    if ord('s') in keys:
        vy = -speed
    if ord('a') in keys:
        vx = -speed
    if ord('d') in keys:
        vx = speed

    p.resetBaseVelocity(robot2, linearVelocity=[vx, vy, 0])
    
    # Control robot with arrow keys
    if p.B3G_LEFT_ARROW in keys:
        vx2 = -speed2
    if p.B3G_RIGHT_ARROW in keys:
         vx2 = speed2
    if p.B3G_UP_ARROW in keys:
         vy2 = speed2
    if p.B3G_DOWN_ARROW in keys:
         vy2 = -speed2

    p.resetBaseVelocity(robot, linearVelocity=[vx2,vy2,0])

# Control arms and grippers for robot (Q/E for arm, R/F for gripper)
    if ord('q') in keys:
        p.setJointMotorControl2(robot, 8, p.POSITION_CONTROL, targetPosition=-0.38)  # extend arm
    if ord('e') in keys:
        p.setJointMotorControl2(robot, 8, p.POSITION_CONTROL, targetPosition=0)  # retract arm
    if ord('r') in keys:
        p.setJointMotorControl2(robot, 9, p.POSITION_CONTROL, targetPosition=0.548)  # open gripper left
        p.setJointMotorControl2(robot, 11, p.POSITION_CONTROL, targetPosition=-0.548)  # open gripper right
    if ord('f') in keys:
        p.setJointMotorControl2(robot, 9, p.POSITION_CONTROL, targetPosition=0)  # close gripper left
        p.setJointMotorControl2(robot, 11, p.POSITION_CONTROL, targetPosition=0)  # close gripper right

    # Control arms and grippers for robot2 (T/Y for arm, U/I for gripper)
    if ord('t') in keys:
        p.setJointMotorControl2(robot2, 8, p.POSITION_CONTROL, targetPosition=-0.38)  # extend arm
    if ord('y') in keys:
        p.setJointMotorControl2(robot2, 8, p.POSITION_CONTROL, targetPosition=0)  # retract arm
    if ord('u') in keys:
        p.setJointMotorControl2(robot2, 9, p.POSITION_CONTROL, targetPosition=0.548)  # open gripper left
        p.setJointMotorControl2(robot2, 11, p.POSITION_CONTROL, targetPosition=-0.548    )  # open gripper right
    if ord('i') in keys:
        p.setJointMotorControl2(robot2, 9, p.POSITION_CONTROL, targetPosition=0)  # close gripper left
        p.setJointMotorControl2(robot2, 11, p.POSITION_CONTROL, targetPosition=0)  # close grippe
