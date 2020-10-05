a=int(input())
b=int(input())
c=int(input())

if a==b==c==0:
  print("inf")
elif a==b==0:
  print("0")
elif a==0 and b!=0:
  print("1")
else:
  delta=b*b-4*(a*c)
  if delta>0:
    print("2")
  if delta==0:
    print("1")
  if delta<0:
    print("0")