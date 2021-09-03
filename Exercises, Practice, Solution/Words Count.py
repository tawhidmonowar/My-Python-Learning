fileName = input('Enter the text file name: ')
file = open(fileName)
counts = dict()

for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

bigCount = 0
bigWord = None

for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print('Big Word:', bigWord, '\nBig Count:', bigCount)