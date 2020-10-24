fh = open('info.txt')
mail=dict()
for line in fh:
    if not line.startswith("X-DSPAM-Processed: ") :
        continue
    else:
        str=line[30:32].rstrip()
        if str not in mail.keys():
            mail.update({str:1})
        else:
            mail[str]+=1
tmp = list()
for v, k in mail.items() :
    tmp.append((v, k))
tmp.sort()
for v,k in tmp:
    print(v,k)
