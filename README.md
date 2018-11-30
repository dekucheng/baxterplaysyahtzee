# baxterplaysyahtzee
##ME495 Final Project: Baxter Robot Plays Yahtzee

## Setup
###Camera Calibration
```
src/detect_checkerboard.py
```

### Baxter
```
rosrun baxter_interface joint_trajectory_action_server.py
rosrun baxter_interface gripper_action_server.py
```

### Baxter Simulator
```
roscore
roslaunch baxter_gazebo baxter_world.launch
rosrun baxter_examples xdisplay_image -f jarvis.jpg
rosrun baxter_tools enable_robot.py -e
rosrun baxter_interface joint_trajectory_action_server.py 
```

### Baxter
```
Connect via Ethernet
```
.roscore
