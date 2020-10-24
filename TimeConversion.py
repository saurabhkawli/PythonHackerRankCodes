s='11:00:45AM'
newtime=''
if s[8:]=='PM':
    sum=12+int(s[0:2])
    newtime=str(sum)+s[2:8]
else:
    newtime=s[:8]
print(s[:8])
print('new ',newtime)
