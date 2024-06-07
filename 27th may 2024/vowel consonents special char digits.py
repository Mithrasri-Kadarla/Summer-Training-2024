s='f46feLK9y56u#@&56hIjbn6KJhA'
'''v=['a','e','i','o','u','A','E','I','O','U']
uv=[]
uc=[]
lv=[]
lc=[]
d=[]
sc=[]
for i in s:
    if i.isupper():
        if i in v:
            uv.append(i)
        else:
            uc.append(i)
    elif i.islower():
        if i in v:
            lv.append(i)
        else:
            lc.append(i)
    elif i.isdigit():
        d.append(i)
    else:
        sc.append(i)'''

lv=0  
uv=0  
lc=0  
uc=0 
d=0  
sp=0 
s="f46feLK9y56u#@&56hIjbn6KJhA"
vow="aeiou"
for i in s:
    if i.islower() and i in vow:
        lv+=1
    elif i.isupper() and i.lower() in vow:
        uv+=1
    elif i.isdigit():
        d+=1
    elif i.islower() and i not in vow:
        lc+=1
    elif i.isupper() and i.lower() not in vow:
        uc+=1
    else:
        sp+=1
print(lv)
print(uv)
print(lc)
print(uc)
print(d)
print(sp)
