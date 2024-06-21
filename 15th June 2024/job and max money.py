jobs = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
m = [5, 6, 5, 4, 11, 2]
b = m.copy()

for i in range(1, len(m)):
    for j in range(0, i):
        if jobs[j][1] <= jobs[i][0]:
            if b[j] + m[i] > b[i]:
                b[i] = b[j] + m[i]

print(b)  
print(max(b))  
