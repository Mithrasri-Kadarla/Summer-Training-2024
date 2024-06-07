n=int(input())
matrix=[]
for i in range(n):
    row=input()
    matrix.append(row)
s=input()
f=0
for i in range(len(s)):
    if s[i] not in matrix[i%n]:
        print("no")
        break
else:
    print("yes")
