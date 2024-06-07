n=int(input())
matrix=[]
for i in range(n):
    row=input()
    matrix.append(row)
s=input()
i=0
for row in matrix:
    if s[i] in row:
        x=1
        i+=1
    else:
        print("no")
        break
else:
    if x:
        print("yes")
