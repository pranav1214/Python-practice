# to read a word and find letter frequency
#i/p: kkammmall {k:2, a:2, m:3, l:2}

word = input("Enter a Word: ")

letter_counter = {}

for w in word:
	co = letter_counter.get(w)
	if co == None:
		letter_counter[w] = 1
	else:
		letter_counter[w] = co + 1

print(letter_counter)