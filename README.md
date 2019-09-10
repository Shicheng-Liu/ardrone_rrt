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
The demo is shown below:

![image](https://github.com/Shicheng-Liu/ardrone_rrt/blob/master/ardrone_rrt_star.gif)
<br>
Compared to RRT, you can find that the path drawn by RRT* is more smooth. That is because before any new vertex added in the tree, the program will search the shortest path around its neighborhood.
<br>
Then, we have a new way called RRT-connect, which is an upgrade version of RRT. It has two differences: 1. Using greedy method, so you will see the length of each step is far longer. 2. Using bidirectional search: both the drone and the target will track the same random vertex.

![image](https://github.com/Shicheng-Liu/ardrone_rrt/blob/master/ardrone_rrt_connect.gif)
<br>
RRT-connect is fast but it will draw a really ugly path: you can see there are sharp corners which make it quite impossible for a drone to follow. From my perspective, RRT-connect may work perfect in a complicated case, such as a maze, since the complicated obstacles wil constraint the lengh of each step. However, in my scenario, obstacles are quite simple so that the length of each edge is quite long.
<br>
To solve this problem, I come up with a new alogrithm called RRT*-connect: sort of like a combination of RRT* and RRT-connect, but without greedy method. It works well and can draw beautiful path.

![image](https://github.com/Shicheng-Liu/ardrone_rrt/blob/master/ardrone_rrt_star_connect.gif)
<br>
It can draw a smooth path but run slow cause it is quite computationally expensive. According, I make an upgrade: only search the surrounding of the newest vertex in the target tree:

![image](https://github.com/Shicheng-Liu/ardrone_rrt/blob/master/ardrone_rrt_star_connect_upgrade.gif)
<br>
Now, it works quite well.
