''' to read two strings and check if they are anagrams
anagrams are same letters but different meaning
'''

def mysort(s):
	d = sorted(s)
	ns = ''.join(d)
	return ns

s1 = input("Enter first string: ")
ns1 = mysort(s1)

s2 = input("Enter second string: ")
ns2 = mysort(s2)

if ns1 == ns2:
	print("Anagram")

else:
	print("Not an Anagram")