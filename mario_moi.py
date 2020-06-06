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

down=0
z=0.01
h=y
a=250
b=280
aa=310
bb=320

a1=150
b1=320
aa1=210
bb1=360


while True:
	up=y-bb
	up1=int(y)-int(bb1)
	xx=x+20
	yy=y+80
	display.fill(black)
	pygame.draw.rect(display,white,(0,0,500,10))
	pygame.draw.rect(display,white,(0,390,500,10))
	pygame.draw.rect(display,white,(0,0,10,400))
	pygame.draw.rect(display,white,(490,0,10,400))
	pygame.draw.rect(display,block,(a,b,59,20))
	pygame.draw.rect(display,block,(a1,b1,59,20))
	pygame.draw.rect(display,blue,(x,y+30,19,50))
	pygame.draw.rect(display,red,(x,y,19,30))


	if x>=470:
		x=470
	if x<=10:
		x=10
	if y>=310:
		y=310
	if y<=10:
		y=10



	if xx<=aa and x>=a and int(yy)==b or xx<=aa1 and x>=a1 and int(yy)==b1:
		down=2
	elif int(yy)==b and xx>aa or int(yy)==b and x<a:
		if down==1:
			down=1
		else:
			down=0
	if down==1:
		z=0.1
		if y==h:
			down=0
	elif down==2:
		z=0
	elif down==0:
		z=0.01	
	y=y+z

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type== pygame.KEYDOWN:

			if event.key==pygame.K_LEFT:
				if x==aa and x>=aa and b>y and b<=yy or x==aa1 and x>=aa1 and b1>y and b1<=yy:
					x=x
				else:
					x=x-20
			elif event.key==pygame.K_RIGHT:
				if xx<=aa and xx==a and b>y and b<=yy or xx<=aa1 and xx==a1 and b1>y and b1<=yy:
						x=x
				else:
					x=x+20
			elif event.key==pygame.K_UP:
				if y<=bb and y>b and xx<=aa and xx>=a and x>=a and x<=aa or y<=bb1 and y>b1 and xx<=aa1 and xx>=a1:
					y=y
				else:
					down=0
					if x>=aa or xx<=a1 or xx<=a and x>=aa1 or up>=60 and x<aa and x>a or up>=60 and xx<aa and xx>a or up1>=60 and x>a1 and x<aa1 or up1>=60 and xx>a1 and xx<aa1 or y<=b or y<=b1:
# condition3xx<=a and x>=aa1, l'obstable0 doit etre a droite de l'obstacle1
						y=y-60

					if up<60 and up>0 and x<aa and xx>a:
						print("a0 "+str(up))
						y=y-up
					if up<60 and up1>0 and x<aa1 and xx>a1:
						print("a1"+str(up1))
						y=y-up1
					
			elif event.key==pygame.K_DOWN:
				down=1

	pygame.display.update()






















