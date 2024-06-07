# ip:
#     15 3 2 7 8 4     |       5 4 2 9 7 1   |      9 8 7 6 5 4   |  5 3 2 7 8 4
#     m  t w t f s     |                     |                    |
# op: -----------------| --------------------|--------------------|---------------
#     6                |      7              |     0              |  6
a= list(map(int, input().split(' ')))
pr=0
for i in range(len(n)-1):
    for j in range(i+1,len(a)):
        if (a[i]<a[j] and a[j]-a[i]>pr):
            pr=a[j]-a[i]
print(pr)
