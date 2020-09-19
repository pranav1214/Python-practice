''' to read two strings and check if they are anagrams
anagrams are same letters but different meaning
'''

s1 = input("Enter first string: ")
ns1 = sorted(s1)
r1 = ''.join(ns1)

d1 = input("Enter second string: ")
nd1 = sorted(d1)
r2 = ''.join(nd1)

if r1 == r2:
	print("Anagram")

else:
	print("Not an Anagram")