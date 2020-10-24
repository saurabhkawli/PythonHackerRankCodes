fh = open('info.txt')
mail=dict()
for line in fh:
    if not line.startswith("From:") :
        continue
    else:
        str=line[6:].rstrip()
        if str not in mail.keys():
            mail.update({str:1})
        else:
            mail[str]+=1
maxvalue=max(mail,key=mail.get)
print(maxvalue,mail[maxvalue])
