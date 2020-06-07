print("combien de chiffre au total")
a=input()
b=int(a)
c=0
f=0
while c<b:
	c=c+1
	if c==1:
		print("quel nombre")
	if c>1:
		print("le prochain nombre")
	d=input()
	e=int(d)
	g=f+e
	print(d+"+"+str(f)+"="+str(g))
	f=g
print(g)
