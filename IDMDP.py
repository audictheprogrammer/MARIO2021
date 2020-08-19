a=0
f=1
id1="admin"
mdp1="admin"
while a==0:
	if f==1:
		print("register(1) ou login(2)")
		c=input()
	else:
		c=2
	if int(c)==1:
		print("ID:")
		id1=input()
		print("password:")
		mdp1=input()
	if int(c)==2:
		print("ID:")
		id2=input()
		print("password:")
		mdp2=input()
		if id2==id1 and mdp2==mdp1:
			print("correct")
			a=3
		else:
			print("forget password?")
			b=input()
			if b=="yes":
				print("new password:")
				mdp1=input()
				f=1
			elif b=="no":
				f=0