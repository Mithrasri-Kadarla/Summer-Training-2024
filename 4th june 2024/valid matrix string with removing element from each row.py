n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(input()))
s=input()
f=0
for i in range(len(s)):
    if s[i] not in matrix[i%n]:
        print("no")
        f=1
        break
    else:
        matrix[i].remove(s[i])
if f==0:
    print("Yes")
