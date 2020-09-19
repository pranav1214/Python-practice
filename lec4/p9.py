'''
read a sentence and sort every word
i/p: kamal classes thane
o/p: aaklm acelsss aehnt
'''

def mysort(s):
	d = sorted(s)
	ns = ''.join(d)
	return ns

sent = input("Enter you sentence: ")

data = sent.split(" ")

newsent = ""

for d in data:
	newsent = newsent + " " + mysort(d)

print(sent, " ", newsent)