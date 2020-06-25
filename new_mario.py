import pygame,sys
from pygame.locals import*
pygame.init()

display_x=500
display_y=400
display=pygame.display.set_mode((display_x,display_y))
white=(255,255,255)
black=(0,0,0)
block=(178,34,34)
red=(255,0,0)
blue=(0,0,255)
x=210
y=310
x_block=[250]
y_block=[280]
l=20
h=80
L=[60]
H=[20]
basic_gravity=0.02
accelerated_gravity=0.1
gravity=basic_gravity
jump=60

while True:
	display.fill(black)
	pygame.draw.rect(display,red,(x,y,l,h-50))
	pygame.draw.rect(display,blue,(x,y+30,l,h-30))
	if len(x_block)==1 and len(y_block)==1:
		pygame.draw.rect(display,block,(x_block[0],y_block[0],L[0],H[0]))
		if x>=x_block[0] and x+l<=x_block[0]+L[0] and int(y+h)==y_block[0]:
			gravity=0
		elif gravity==0 and (x<x_block[0] or x+l>x_block[0]):
			gravity=basic_gravity
			

	for event in pygame.event.get():
		if len(x_block)==1 and len(y_block)==1:
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					if x+l<=x_block[0] or x>x_block[0]+L[0] or int(y+h)<=y_block[0] or int(y)>=y_block[0]+H[0]:
						x=x-l
					
				elif event.key==pygame.K_RIGHT:
					if x>=x_block[0]+L[0] or x+l<x_block[0] or int(y+h)<=y_block[0] or int(y)>=y_block[0]+H[0]:
						x=x+l
				elif event.key==pygame.K_UP:
					if int(y+h)<=y_block[0] or x>=x_block[0]+L[0] or x+l<=x_block[0]:
						y=y-jump
					if int(y)>y_block[0]+H[0]:
						y=y-int(y-(y_block[0]+H[0]))
					gravity=basic_gravity
					#not sure about that, maybe after (y-jump and y-int)
				elif event.key==pygame.K_DOWN:
					gravity=accelerated_gravity

				






		if event.type==QUIT:
			pygame.quit()
			sys.exit()





	

	x=max(x,0)
	x=min(x,display_x-l)
	y=max(y,0)
	y=min(y,display_y-h)
	
	y=y+gravity
	






















	pygame.display.update()


