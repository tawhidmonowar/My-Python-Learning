x = open('data.txt')
counts = dict()
for line in x:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, value in counts.items():
    newTup = (value, key)
    lst.append(newTup)

lst = sorted(lst, reverse=True)
for value, key in lst[:3]:
    print(key, value)
