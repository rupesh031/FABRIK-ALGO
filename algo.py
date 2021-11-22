import pygame
import math
def distance(p,t):
	return math.sqrt((p[0]-t[0])**2+(p[1]-t[1])**2)    
def unitvector(x,y):
	return ((x[0]-y[0])/(math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)),(x[1]-y[1])/(math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)))
	

def drawlines(l,c):
	i=0
	while i<len(l)-1:
		pygame.draw.line(screen,c,l[i],l[i+1],2)
		i+=1
	pygame.display.flip()
	pygame.display.update()

def forward():
	global status
	global points
	i=0
	f=0
	while i<=len(points)-2:
		unitvec=unitvector(points[i+1],points[i])
		d=distance(points[i+1],points[i])
		points[i+1]=(points[i][0]+dlist[f]*unitvec[0],points[i][1]+dlist[f]*unitvec[1])
		i+=1
		f+=1
	if d2-0.52<distance(points[-1],points[-2]) and d2+0.52>distance(points[-1],points[-2]):
		status=True
		print("done")
	

def backward():
	global status
	global points
	points.pop(-2)
	i=len(points)-1
	f=len(dlist)-1
	print(i)
	while i>=2:
		unitvec=unitvector(points[i-1],points[i])
		points[i-1]=(points[i][0]+dlist[f]*unitvec[0],points[i][1]+dlist[f]*unitvec[1])
		f-=1
		i-=1
	
	if d1-0.52<distance(points[0],points[1]) and d1+0.52>distance(points[0],points[1]):
		status=True
		print(points)
		print("done")
	
def eachdis():
	print("new call")
	i=0
	while i<=len(points)-2:
		print(distance(points[i],points[i+1]))
		dlist.append(distance(points[i],points[i+1]))
		i+=1
	dlist.pop()


points=[]
target=False
background_colour = (255,255,255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('FABRIK')
screen.fill(background_colour)
clock = pygame.time.Clock()
pygame.display.flip()
running = True
status=False
dlist=[]
f=0

while running:
	for event in pygame.event.get():
	  if event.type == pygame.QUIT:
		  running = False
	  if event.type == pygame.MOUSEBUTTONDOWN:
		  p=pygame.mouse.get_pos()
		  if not target:
			  points.append(p)
		  if f==0 and event.button==1:
			  f+=1
			  pygame.draw.circle(screen,"yellow",p,4)
		  elif event.button==3 and not target:
			  target=True
			  d1=distance(points[0],points[1])
			  d2=distance(points[-2],points[-3])
			  print(points)
			  pygame.draw.circle(screen,"red",p,4)
		  elif event.button==1 and not target:
			  pygame.draw.circle(screen,"black",p,4)
		  elif event.button==2:
			  target=False
			  status=False
			  a=points.pop()
			  pygame.draw.circle(screen,"white",a,4)
			  
	if target and not status:
		drawlines(points[0:-1],"black")
		eachdis()
		while not status:
			backward()
			forward()	
		drawlines(points,"blue")	
		eachdis()	
		for i in points[1:-1]:
			pygame.draw.circle(screen,"black",i,4)
			  
		  
	pygame.display.update()
	clock.tick(30)
    
