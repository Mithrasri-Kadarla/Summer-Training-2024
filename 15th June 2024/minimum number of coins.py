c=[1,2,4,5]
n=int(input())
c=c[::-1]
for i in c:
    if n%i==0:
        print(n//i)
        break
    
