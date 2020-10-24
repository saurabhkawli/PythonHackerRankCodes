fh = open('word.txt')
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        count+=1
        total+=float(line[line.find('0'):len(line)+1])
avg = total/count
print('Average spam confidence:',avg)


