fh = open('info.txt')
count=0
for line in fh:
    line.split()
    if not line.startswith("From:") :
        continue
    else:
        count+=1
        print(line[5:].rstrip())
print("There were", count, "lines in the file with From as the first word")

