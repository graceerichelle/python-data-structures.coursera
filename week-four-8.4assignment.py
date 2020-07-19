fname = input("Enter file name: ")
fh = open(fname)
collection = fh.read()
wordlist = list()

for wordloop in collection.split():
    value = wordloop
    if value in wordlist:
        continue
    wordlist.append(value)

wordlist.sort()
print(wordlist)
