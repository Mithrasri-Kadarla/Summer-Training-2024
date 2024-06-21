n = int(input("Enter a number: "))
s = str(n)
l = len(s)

if l % 2 == 0:
    fh = s[:l // 2]
    mirror = fh + fh[::-1]
    if int(mirror) <= n:
        fh = str(int(fh) + 1)
        mirror = fh + fh[::-1]
else:
    fh = s[:l // 2 + 1]
    mirror = fh + fh[:-1][::-1]
    if int(mirror) <= n:
        fh = str(int(fh) + 1)
        mirror = fh + fh[:-1][::-1]

print(mirror)
