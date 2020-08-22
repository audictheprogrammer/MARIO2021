import math
a=float(input())
b=float(input())
sqrt_module=math.sqrt(a**2+b**2)
print("mod= "+str(sqrt_module))

cos=a/sqrt_module
sin=b/sqrt_module
arccos=math.acos(cos)
arcsin=math.asin(sin)

if cos>0 and sin>0:
	teta=arccos
if cos<0 and sin>0:
	teta=arccos #or arcsin+pi/2
if cos<0 and sin<0:
	teta=-arccos
if cos>0 and sin<0:
	teta=arcsin #or -arccos
print("arg= "+ str(teta))






