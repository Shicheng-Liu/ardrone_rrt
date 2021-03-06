import sys, random, math, pygame, time
from pygame.locals import *
from math import *

length=500
width=700
step_length=10
vertex_number=2000

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
    neighborhood_calculated=500*sqrt(log(count)/count)
    if neighborhood_calculated<18:
      return neighborhood_calculated
    else:
      return 18

def collision_test(new_vertex,vertex):    
    k=(new_vertex.y-vertex.y)/(new_vertex.x-vertex.x)
    if (new_vertex.x<280 and new_vertex.y>400 and new_vertex.y<420) or (new_vertex.x>220 and new_vertex.y>250 and new_vertex.y<270):
      print("delete this new vertex because of collision")
      return 0
    elif (new_vertex.y-400)*(vertex.y-400)<0 and (new_vertex.x-280)*(vertex.x-280)<0 and vertex.y+k*(280-vertex.x)>400:
      print("delete this new vertex because of collision")
      return 0
    elif (new_vertex.y-420)*(vertex.y-420)<0 and (new_vertex.x-280)*(vertex.x-280)<0 and vertex.y+k*(280-vertex.x)<420:
      print("delete this new vertex because of collision")
      return 0
    elif (new_vertex.y-250)*(vertex.y-250)<0 and (new_vertex.x-220)*(vertex.x-220)<0 and vertex.y+k*(220-vertex.x)>250:
      print("delete this new vertex because of collision")
      return 0
    elif (new_vertex.y-270)*(vertex.y-270)<0 and (new_vertex.x-220)*(vertex.x-220)<0 and vertex.y+k*(220-vertex.x)<270:
      print("delete this new vertex because of collision")
      return 0
    else:
      return 1


def path_choose(tree, drone, target):
    vertex=tree[0]
    for x in tree:
      if distance([x.x,x.y],[target.x,target.y])<distance([vertex.x,vertex.y],[target.x,target.y]):
        vertex=x
    while vertex!=drone:
      pygame.draw.line(screen,blue,[vertex.x,vertex.y],[vertex.last.x,vertex.last.y],5)
      vertex=vertex.last
      pygame.display.flip()

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
        sign=1
        for i in range(vertex_number):
          print "number = %d" %sign
          sign=sign+1
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
          sign_1=collision_test(new_vertex,new_vertex.last)
          if sign_1==1:
            for x in tree:
              if distance([x.x,x.y],[new_vertex.x,new_vertex.y])<neighborhood and x.cost+distance([x.x,x.y],[new_vertex.x,new_vertex.y])<new_vertex.cost:
                sign_2=collision_test(new_vertex,x)
                if sign_2==1:
                  new_vertex.last=x
                  new_vertex.cost=x.cost+distance([x.x,x.y],[new_vertex.x,new_vertex.y]) 
            tree.append(new_vertex)
            pygame.draw.line(screen,black,[new_vertex.last.x,new_vertex.last.y],[new_vertex.x,new_vertex.y])
            pygame.display.flip()
          else:
            continue
          
          for i in xrange(len(tree)):
            x=tree[i]
            if x!=new_vertex.last and distance([x.x,x.y],[new_vertex.x,new_vertex.y])<neighborhood and distance([x.x,x.y],[new_vertex.x,new_vertex.y])+new_vertex.cost<x.cost:
              sign_3=collision_test(x,new_vertex)
              if sign_3==1:
                pygame.draw.line(screen,white,[x.x,x.y],[x.last.x,x.last.y])
                x.last=new_vertex
                x.cost=distance([x.x,x.y],[new_vertex.x,new_vertex.y])+new_vertex.cost
                tree[i]=x
                pygame.draw.line(screen,black,[x.x,x.y],[x.last.x,x.last.y])
                pygame.display.flip()

          pygame.draw.circle(screen,red,(x1,y1),radius_1,0)
          pygame.draw.circle(screen,green,(x2,y2),radius_2,0)
          pygame.draw.rect(screen, (0,0,0), (0,400,280,20), 0)
          pygame.draw.rect(screen, (0,0,0), (220,250,280,20), 0)
          pygame.display.flip()
        path_choose(tree,drone,target)

    
    






