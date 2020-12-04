from fltk import *

#conversion
def f(x,interval):
	return (x-200)/(200/interval)
def g(y,interval):
	return (-(200/interval)*y)+200
#polynomial
def h(x):
  sum=0
  for i in range(len(list)):
    sum+= list[i] * x **(i)
  return sum

#input
list=[]

n=int(input("whats the max degree of the polynomial\n"))
for i in range(n+1):
	a=int(input(f"coefficient of X degree{i}\n"))
	list.append(a)
print(list)

interval=float(input("interval?\n"))

cree_fenetre(400,400)#display

#drawing axes
ligne(0,200,400,200)
fleche(0,200,400,200,"black",3)
ligne(200,400,200,0)
fleche(200,400,200,0,"black",3)

texte(370,205,str(interval),taille=12)
texte(5,205,str(-interval),taille=12)
texte(170,0,str(interval),taille=12)
texte(170,370,str(-interval),taille=12)


#quick maths
for x in range(1,400):
	ligne(x-1,g(h(f(x-1,interval)),interval),x,g(h(f(x,interval)),interval),"red")
	print(x,f(x,interval),h(f(x,interval)),g(h(f(x,interval)),interval))
	

#to allow to close the tk window
attend_clic_gauche()
