import pygame,sys
from pygame.locals import*
pygame.init()

display=pygame.display.set_mode((1500,400))
#redgreenblue
white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
block=(178,34,34)
x=210
y=310
h=80
l=20


down=0
v=0.01 # vitesse de gravite
vv=0.1 # vitesse de descente accelere
z=v

hh=y
#a=250
#b=280
#aa=310
#bb=320
#
a=[250,150]#
b=[280,320]#
L=60
H=20
#
#a1=150
#b1=320
#aa1=210
#bb1=360


while True:

	up=y-b[0]+H
	up1=int(y)-int(b[1]+H)
	xx=x+l
	yy=y+h
	display.fill(black)
	pygame.draw.rect(display,white,(0,0,500,10))
	pygame.draw.rect(display,white,(0,390,500,10))
	pygame.draw.rect(display,white,(0,0,10,400))
	pygame.draw.rect(display,white,(490,0,10,400))
	pygame.draw.rect(display,block,(a[0],b[0],59,20))
	pygame.draw.rect(display,block,(a[1],b[1],59,20))
	pygame.draw.rect(display,blue,(x,y+30,l-1,h-30))
	pygame.draw.rect(display,red,(x,y,l-1,h-50))


	if x>=470:
		x=470
	if x<=10:
		x=10
	if y>=310:
		y=310
	if y<=10:
		y=10



	if x+l<=a[0]+L and x>=a[0] and int(y+h)==b or x+L<=a[1] and x>=a[1] and int(y+h)==b[1]:
		down=2
	elif int(y+h)==b[0] and x+l>a[0]+L or int(y+h)==b[0] and x<a[0]:
		if down==1:
			down=1
		else:
			down=0
	if down==1:
		z=vv
		if y==hh:
			down=0
	elif down==2:
		z=0
	elif down==0:
		z=v	
	y=y+z

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type== pygame.KEYDOWN:

			if event.key==pygame.K_LEFT:
				if x==a[0]+L and x>=a[0]+L and b[0]>y and b[0]<=y+h or x==a[1]+L and x>=a[1]+L and b[1]>y and b[1]<=y+h:
					x=x
				else:
					x=x-l
			elif event.key==pygame.K_RIGHT:
				if x+l<=a[0]+L and x+l==a[0] and b[0]>y and b[0]<=y+h or x+l<=a[1]+L and x+l==a[1] and b[1]>y and b[1]<=y+h:
						x=x
				else:
					x=x+l
			elif event.key==pygame.K_UP:
				if y<=b[0]+H and y>b[0] and x+l<=a[0]+L and x+l>=a[0] and x>=a[0] and x<=a[0]+L or y<=b[1]+H and y>b[1] and x+l<=a[1]+L and x+l>=a[1]:
					y=y
				else:
					down=0
					if 







						y=y-60

					if up<60 and up>0 and x<a[0]+L and x+l>a[0]:
						print("a0 "+str(up))
						y=y-up
					if up<60 and up1>0 and x<a[1]+L and x+l>a[1]:
						print("a1"+str(up1))
						y=y-up1
					
			elif event.key==pygame.K_DOWN:
				down=1

	pygame.display.update()






















