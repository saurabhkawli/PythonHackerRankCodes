fh = open('word.txt')
lst = list()
for line in fh:
    word = line.split()
    for wd in word:

        if wd not in lst:
            lst.append(wd)
        else:
            continue
lst.sort()
print(lst)
