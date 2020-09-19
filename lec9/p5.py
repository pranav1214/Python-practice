from datetime import *

d = datetime.now()
h = d.hour


if( h >=6 and h <12):
	print("Good Morning")
elif( h>=12 and h< 17 ):
	print("Good Afternon")
else:
	print("Good Evening")
