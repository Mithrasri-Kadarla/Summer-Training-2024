s="MMMFFFFMMFMFMFMFMFMMMMFFFFFFFFMFMF"
m=0
f=0
for i in s:
    if i=="M":
        m+=1
    else:
        f+=1
print("Male:",m)
print("Female:",f)
if m==f:
    print(0)
elif m>f:
    print("Male")
elif f>m:
    print("Female")
