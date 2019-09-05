 ardrone_rrt
 ==
 This repository documents some works about RRT on ardrone, including RRT and RRT* simulation(python script), ROS package of RRT and RRT* motion planning for ardrone.
 <br>
 
 Simulation(python script)
 ----
 In this repo, you can see two python scripts: _ardrone_rrt_, _ardrone_rrt_star_. These are simulations of this project.
 <br>
 After downloading this reposity, you can _cd_ to the directory you download, then run:
 ```
 python ardrone_rrt.py
 ```
 You can use this simulation: You can click on somewhere and a red circle will show at the place you click, which means the drone is set. Then you can click on another place. A green circle representing target will show at the place. The two black rectangles represent the obstacles in our lab. Demo is shown below:
![image](https://github.com/Shicheng-Liu/ardrone_rrt/blob/master/ardrone_rrt.gif) 
<br>
There is another simulation which records the performace of RRT*, run:
```
python ardrone_rrt_star.py
```
The deom is shown below:

![image](https://github.com/Shicheng-Liu/ardrone_rrt/blob/master/ardrone_rrt_star.gif)
<br>
Compared to RRT, you can find that the path drawn by RRT* is more smooth. That is because before any new vertex added in the tree, the program will search the shortest path around its neighborhood.
