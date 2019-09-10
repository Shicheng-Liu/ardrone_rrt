import sys, random, math, pygame, time
from pygame.locals import *
from math import *

length=500
width=700
step_length=10
vertex_number=7000

running=1
pygame.init()
screen = pygame.display.set_mode((length,width))
pygame.display.set_caption('ardrone_rrt_star')
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
x1=0
y1=0
x2=0
y2=0
radius=10
radius_1=0
radius_2=0
count=0

def distance(x1,x2):
  return sqrt((x1[0]-x2[0])*(x1[0]-x2[0])+(x1[1]-x2[1])*(x1[1]-x2[1]))

def step(x1,x2):
  if distance(x1,x2)<=step_length:
    return x2
  else:
    angle=atan2(x2[1]-x1[1],x2[0]-x1[0])
    return x1[0]+step_length*cos(angle), x1[1]+step_length*sin(angle)  

class point:
    x=0
    y=0
    last=None
    cost=0
    def __init__(self,x_value,y_value):
         self.x=x_value
         self.y=y_value

def choose_neighborhood(tree):
    count=len(tree)
    neighborhood_calculated=1200*sqrt(log(count)/count)
    if neighborhood_calculated<30:
      return neighborhood_calculated
    else:
      return 30

def oscillation_test(new_vertex):    #a safe distance of 10 from obstacles
    k=(new_vertex.y-new_vertex.last.y)/(new_vertex.x-new_vertex.last.x)
    if (new_vertex.x<290 and new_vertex.y>390 and new_vertex.y<430) or (new_vertex.x>210 and new_vertex.y>240 and new_vertex.y<280):
      print("delete this new vertex because of oscillation")
    elif (new_vertex.y-390)*(new_vertex.last.y-390)<0 and (new_vertex.x-290)*(new_vertex.last.x-290)<0 and new_vertex.last.y+k*(290-new_vertex.last.x)>390:
      print("delete this new vertex because of oscillation")
    elif (new_vertex.y-430)*(new_vertex.last.y-430)<0 and (new_vertex.x-290)*(new_vertex.last.x-290)<0 and new_vertex.last.y+k*(290-new_vertex.last.x)<430:
      print("delete this new vertex because of oscillation")
    elif (new_vertex.y-240)*(new_vertex.last.y-240)<0 and (new_vertex.x-210)*(new_vertex.last.x-210)<0 and new_vertex.last.y+k*(210-new_vertex.last.x)>240:
      print("delete this new vertex because of oscillation")
    elif (new_vertex.y-280)*(new_vertex.last.y-280)<0 and (new_vertex.x-210)*(new_vertex.last.x-210)<0 and new_vertex.last.y+k*(210-new_vertex.last.x)<280:
      print("delete this new vertex because of oscillation")
    else:
      tree.append(new_vertex)

while running: 
    screen.fill(white) 
    pygame.draw.circle(screen,red,(x1,y1),radius_1,0)
    pygame.draw.circle(screen,green,(x2,y2),radius_2,0)
    pygame.draw.rect(screen, (0,0,0), (0,400,280,20), 0)
    pygame.draw.rect(screen, (0,0,0), (220,250,280,20), 0)
    #pygame.display.flip()  
    tree = []
    event=pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      count=count+1
      if count== 1:
        x1,y1=pygame.mouse.get_pos()
        radius_1=10
        pygame.draw.circle(screen,red,(x1,y1),radius_1,0)
        pygame.display.flip()
      elif count==2:
        x2,y2=pygame.mouse.get_pos()
        radius_2=10
        tree.append(point(x1,y1))
        drone=tree[0]
        target=point(x2,y2)
        
        for i in range(vertex_number):
          vertex_random=point(random.random()*length, random.random()*width)
          vertex = tree[0]
          for x in tree:                
            if distance([x.x,x.y],[vertex_random.x,vertex_random.y])<distance([vertex.x,vertex.y],[vertex_random.x,vertex_random.y]):
              vertex=x
          new=step([vertex.x,vertex.y],[vertex_random.x,vertex_random.y])
          new_vertex=point(new[0],new[1])
          new_vertex.last=vertex
          new_vertex.cost=vertex.cost+distance([x.x,x.y],[vertex_random.x,vertex_random.y])
          neighborhood=choose_neighborhood(tree)
          for x in tree:
            if distance([x.x,x.y],[new_vertex.x,new_vertex.y])<neighborhood and x.cost+distance([x.x,x.y],[new_vertex.x,new_vertex.y])<new_vertex.cost:
              new_vertex.last=x
              new_vertex.cost=x.cost+distance([x.x,x.y],[new_vertex.x,new_vertex.y]) 
          oscillation_test(new_vertex)
          pygame.draw.line(screen,black,[vertex.x,vertex.y],[new_vertex.x,new_vertex.y])
          pygame.display.flip()
          if distance([new_vertex.x,new_vertex.y],[target.x,target.y])<radius:
            print("finished")
            while new_vertex!=drone:
              pygame.draw.line(screen,blue,[new_vertex.x,new_vertex.y],[new_vertex.last.x,new_vertex.last.y],5)
              new_vertex=new_vertex.last
              pygame.display.flip()
            break
          pygame.draw.circle(screen,red,(x1,y1),radius_1,0)
          pygame.draw.circle(screen,green,(x2,y2),radius_2,0)
          pygame.draw.rect(screen, (0,0,0), (0,400,280,20), 0)
          pygame.draw.rect(screen, (0,0,0), (220,250,280,20), 0)
          pygame.display.flip()

    
    






