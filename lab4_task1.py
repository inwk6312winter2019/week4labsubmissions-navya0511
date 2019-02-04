import string

fin=open('emma.txt')
name=fin.read()
for line in name.split():
	word=line.strip(string.punctuation)
	print(word.lower())

