import sys, random, math, pygame, time
from pygame.locals import *
from math import *

length=500
width=700
#step_length=10
vertex_number=5000

running=1
pygame.init()
screen = pygame.display.set_mode((length,width))
pygame.display.set_caption('ardrone_rrt_connect')
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

def step(x1,x2):  # greedy strategy
  k = (x2[1]-x1[1])/(x2[0]-x1[0])
  b = x1[1]-k*x1[0]
  count = 0
  # collision test: safe distance of 10 from obstacles
  if (x1[1]-430)*(x2[1]-430)<=0 and (430-b)/k<=290:
    count+=1
  if (x1[1]-390)*(x2[1]-390)<=0 and (390-b)/k<=290:
    count+=1
  if (x1[0]-290)*(x2[0]-290)<=0 and k*290+b>=390 and k*290+b<=430:
    count+=1
  if (x1[1]-240)*(x2[1]-240)<=0 and (240-b)/k>=210:
    count+=1
  if (x1[1]-280)*(x2[1]-280)<=0 and (280-b)/k>=210:
    count+=1
  if (x1[0]-210)*(x2[0]-210)<=0 and k*210+b>=240 and k*210+b<=280:
    count+=1
  print "count=%d" %count
  if count==1:
    if (x1[1]-430)*(x2[1]-430)<=0 and (430-b)/k<=290:
      if x1[1]==430:
        if x2[1]>=430:
          return x2[0],x2[1]
        else:
          return x1[0],x1[1]
      else:
        return (430-b)/k, 430
    elif (x1[1]-390)*(x2[1]-390)<=0 and (390-b)/k<=290:
      if x1[1]==390:
        if x2[1]<=390:
          return x2[0],x2[1]
        else:
          return x1[0],x1[1]
      else:
        return (390-b)/k, 390
    elif (x1[0]-290)*(x2[0]-290)<=0 and k*290+b>=390 and k*290+b<=430:
      if x1[0]==290:
        if x2[0]>=290:
          return x2[0],x2[1]
        else:
          return x1[0],x1[1]
      else:
        return 290, k*290+b
    elif (x1[1]-240)*(x2[1]-240)<=0 and (240-b)/k>=210:
      if x1[1]==240:
        if x2[1]<=240:
          return x2[0],x2[1]
        else:
          return x1[0],x1[1]
      else:
        return (240-b)/k, 240 
    elif (x1[1]-280)*(x2[1]-280)<=0 and (280-b)/k>=210:
      if x1[1]==280:
        if x2[1]>=280:
          return x2[0],x2[1]
        else:
          return x1[0],x1[1]
      else:
        return (280-b)/k, 280
    elif (x1[0]-210)*(x2[0]-210)<=0 and k*210+b>=240 and k*210+b<=280:
      if x1[0]==210:
        if x2[0]<=210:
          return x2[0],x2[1]
        else:
          return x1[0],x1[1]
      else:
        return 210, 210*k+b
    else:
      print("new occassion 1")
      return x1[0],x1[1]

  elif count==2:
    if ((x1[1]-430)*(x2[1]-430)<=0 and (430-b)/k<=290) and ((x1[1]-390)*(x2[1]-390)<=0 and (390-b)/k<=290):
      if x1[1]>=430:
        return (430-b)/k, 430
      elif x1[1]<=390:
        return (390-b)/k, 390
      else:
        print("new occassion 2")
        return x1[0],x1[1]
    elif ((x1[1]-240)*(x2[1]-240)<=0 and (240-b)/k>=210) and ((x1[1]-280)*(x2[1]-280)<=0 and (280-b)/k>=210):
      if x1[1]>=280:
        return (280-b)/k, 280
      elif x1[1]<=240:
        return (240-b)/k, 240
      else:
        print("new occassion 3")
        return x1[0],x1[1]
    elif ((x1[1]-430)*(x2[1]-430)<=0 and (430-b)/k<=290) and ((x1[0]-290)*(x2[0]-290)<=0 and k*290+b>=390 and k*290+b<=430):
      if x1[1]>=430:
        return (430-b)/k, 430
      else:
        return 290, k*290+b
    elif ((x1[1]-390)*(x2[1]-390)<=0 and (390-b)/k<=290) and ((x1[0]-290)*(x2[0]-290)<=0 and k*290+b>=390 and k*290+b<=430): 
      if x1[1]<=390:
        return (390-b)/k, 390  
      else:
        return 290, k*290+b
    elif ((x1[1]-240)*(x2[1]-240)<=0 and (240-b)/k>=210) and ((x1[0]-210)*(x2[0]-210)<=0 and k*210+b>=240 and k*210+b<=280): 
      if x1[1]<=240:
        return (240-b)/k, 240
      else:
        return 210, 210*k+b
    elif ((x1[1]-280)*(x2[1]-280)<=0 and (280-b)/k>=210) and ((x1[0]-210)*(x2[0]-210)<=0 and k*210+b>=240 and k*210+b<=280):
      if x1[1]>=280:
        return (280-b)/k, 280
      else:
        return 210, 210*k+b
    elif ((x1[1]-390)*(x2[1]-390)<=0 and (390-b)/k<=290) and ((x1[1]-280)*(x2[1]-280)<=0 and (280-b)/k>=210):
      return x1[0],x1[1]
    elif ((x1[0]-290)*(x2[0]-290)<=0 and k*290+b>=390 and k*290+b<=430) and ((x1[1]-280)*(x2[1]-280)<=0 and (280-b)/k>=210):
      return x1[0],x1[1]
    elif ((x1[1]-390)*(x2[1]-390)<=0 and (390-b)/k<=290) and ((x1[0]-210)*(x2[0]-210)<=0 and k*210+b>=240 and k*210+b<=280): 
      return x1[0],x1[1]
    else:
      print("new occassion")
      return x1[0],x1[1]
      print "coordinate %d  %d" %x1[0] %x1[1]
     
  elif count==3 or count==4:
    if x1[1]>=430:
      return (430-b)/k, 430
    elif x1[1]<=240:
      return (240-b)/k, 240
    elif x1[1]<430 and x1[1]>=390:
      return (280-b)/k, 280
    elif x1[1]>240 and x1[1]<=280:
      return (390-b)/k, 390

  else: 
    return x2[0], x2[1]
 


class point:
    x=0
    y=0
    last=None
    def __init__(self,x_value,y_value):
         self.x=x_value
         self.y=y_value


while running: 
    screen.fill(white) 
    pygame.draw.circle(screen,red,(x1,y1),radius_1,0)
    pygame.draw.circle(screen,green,(x2,y2),radius_2,0)
    pygame.draw.rect(screen, (0,0,0), (0,400,280,20), 0)
    pygame.draw.rect(screen, (0,0,0), (220,250,280,20), 0)
    #pygame.display.flip()  
    tree = []
    tree_1=[]
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
        tree_1.append(point(x2,y2))
        target=tree_1[0]
        
        for i in range(vertex_number):
          vertex_random=point(random.random()*length, random.random()*width)
          vertex = tree[0]
          vertex_1=tree_1[0]
          for x in tree:                
            if distance([x.x,x.y],[vertex_random.x,vertex_random.y])<distance([vertex.x,vertex.y],[vertex_random.x,vertex_random.y]):
              vertex=x
          for x in tree_1:                
            if distance([x.x,x.y],[vertex_random.x,vertex_random.y])<distance([vertex_1.x,vertex_1.y],[vertex_random.x,vertex_random.y]):
               vertex_1=x
          new=step([vertex.x,vertex.y],[vertex_random.x,vertex_random.y])
          new_1=step([vertex_1.x,vertex_1.y],[vertex_random.x,vertex_random.y])
          new_vertex=point(new[0],new[1])
          new_vertex_1=point(new_1[0],new_1[1])
          new_vertex.last=vertex
          tree.append(new_vertex)
          new_vertex_1.last=vertex_1
          tree_1.append(new_vertex_1)   
          pygame.draw.line(screen,black,[vertex.x,vertex.y],[new_vertex.x,new_vertex.y])
          pygame.draw.line(screen,black,[vertex_1.x,vertex_1.y],[new_vertex_1.x,new_vertex_1.y])
          pygame.display.flip()
          for x in tree:
            for y in tree_1:
              if distance([x.x,x.y],[y.x,y.y])<distance([new_vertex.x,new_vertex.y],[new_vertex_1.x,new_vertex_1.y]) and distance([x.x,x.y],[y.x,y.y])<radius:
                new_vertex=x  
                new_vertex_1=y                       
          if distance([new_vertex.x,new_vertex.y],[new_vertex_1.x,new_vertex_1.y])<radius: 
            print('finished!')                     
            while new_vertex!=drone:
              pygame.draw.line(screen,blue,[new_vertex.x,new_vertex.y],[new_vertex.last.x,new_vertex.last.y],5)
              new_vertex=new_vertex.last
              pygame.display.flip()
            while new_vertex_1!=target:
              pygame.draw.line(screen,blue,[new_vertex_1.x,new_vertex_1.y],[new_vertex_1.last.x,new_vertex_1.last.y],5)
              new_vertex_1=new_vertex_1.last
              pygame.display.flip()
            break
          pygame.draw.circle(screen,red,(x1,y1),radius_1,0)
          pygame.draw.circle(screen,green,(x2,y2),radius_2,0)
          pygame.draw.rect(screen, (0,0,0), (0,400,280,20), 0)
          pygame.draw.rect(screen, (0,0,0), (220,250,280,20), 0)
          pygame.display.flip()

    
    






