## Sorting the sentence
s="is2 sentence4 This1 a3"
l=[]
for i in s.split(' '):
    l.insert(int(i[-1])-1,i[:-1])
x=' '.join(l)
print(x)
