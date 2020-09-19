# to read a sentence and find the word frequency
# i/p: india america friend india india friend
# o/p: {'india':3, 'america':1, 'friend':2}

sentence = input("Enter a Sentence: ")

data = sentence.split(" ")

word_counter = {}
for w in data:
	co = word_counter.get(w)
	if co == None:
		word_counter[w] = 1

	else:
		word_counter[w] = co + 1

print(word_counter)