import pygame,sys
from pygame.locals import*
pygame.init()

display=pygame.display.set_mode((500,400))
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

upup=60 #hauteur du jump
down=0
v=0.01 # vitesse de gravite
vv=0.2 # vitesse de descente accelere
z=v

hh=y
#a=250
#b=280
#aa=310
#bb=320
#
a=[150,250]#
b=[280,280]#b=320
L=60
H=20
#
#a1=150
#b1=320
#aa1=210
#bb1=360
ok=0


while True:
	for w in range(len(a)):
		up=[int(y-b[0]-H),int(y-int(b[1])-H)]
	
		#up=y-b[0]-H
		#up1=int(y)-int(b[1]-H)
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
	
		for ww in range(len(b)):
			if int(y)+h==b[ww] and a[ww]<=x and a[ww]+L>=x+l:
				down=2
		if down==2:
			z=0
		if down==0:
			z=v	
		y=y+z
	
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type== pygame.KEYDOWN:

				if event.key==pygame.K_LEFT:
					if x==a[0]+L and b[0]>y and b[0]<=y+h or x==a[0]+L and b[0]+H>y and b[0]+H<=y+h or x==a[1]+L and x>=a[1]+L and b[1]>y and b[1]<=y+h or x==a[1]+L and x>=a[1]+L and b[1]+H>y and b[1]+H<=y+h:
						x=x
					else:
						x=x-l

				elif event.key==pygame.K_RIGHT:
					if x+l<=a[0]+L and x+l==a[0] and b[0]>y and b[0]<=y+h or x+l<=a[0]+L and x+l==a[0] and b[0]+H>y and b[0]+H<=y+h or x+l<=a[1]+L and x+l==a[1] and b[1]>y and b[1]<=y+h or x+l<=a[1]+L and x+l==a[1] and b[1]+H>y and b[1]+H<=y+h:
						x=x
					else:
						x=x+l
	
					


				elif event.key==pygame.K_UP:
					if len(a)==1:
						if x<a[0] or x+l>a[0]+L or up[0]>upup or y+h>=b[0]:
							y=y-upup
							down=0
					if len(a)>=2:
						if x+l<=a[0]or x>=a[len(a)-1]+L:
							y=y-upup
							down=0
							ok=1
						for w in range(len(a)-1):
							if y<b[w] or y+h<b[w+1]:
								if up[w+1]<0 or up[0]<0:
								
									y=y-upup
									down=0
							if x>=a[w]+L and x+l<=a[w+1]:
								if ok==0:
									y=y-upup
									down=0
								elif ok==1:
									ok=0

						if up[0]<upup and up[0]>0 and x<a[0]+L and x+l>a[0]:							
							y=y-up[0]
	
						if up[0]<upup and up[1]>0 and x<a[1]+L and x+l>a[1]:
							y=y-up[1]
					
				elif event.key==pygame.K_DOWN:
					down=1

		pygame.display.update()






















