l=input()
d=0.0
e=0
o=0
for i in l.split(' '):
    if '.' in i:
        d+=float(i)
    else:
        if int(i)%2==0:
            e+=int(i)
        elif int(i)%2!=0:
            o+=int(i)

print('decimal sum:',d)
print('even sum:',e)
print('odd sum:',o)
