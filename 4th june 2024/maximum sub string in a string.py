def sub_string(s):
    if not s:
        return 0
    maximum=1
    length=1
    n=len(s)
    for i in range(1,n):
        if s[i]==chr(ord(s[i-1])+1):
            length+=1
        else:
            maximum=max(maximum,length)
            length=1
    maximum=max(maximum,length)
    return maximum
s="abcde"
r=sub_string(s)
print(r)
