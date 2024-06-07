a='bvec'
b=30
c=b%26
d=''
for i in a:
    if ((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
        d+=chr(ord(i)-c+26)
print(d)
