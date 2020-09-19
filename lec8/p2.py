# wapp to read int from CLA adn fin sqrt
# try except else raise


import sys
import math

try:
	num = int(sys.argv[1])
	if num < 0:
		raise Exception ("-ve number not supported")
	res = math.sqrt(num)
except IndexError:
	print("u need to pass 1 integer argument from command line")
except ValueError:
	print("u need to pass integer only")
except Exception as e:
	print("issue", e)
else:
	print("Res= ",res)