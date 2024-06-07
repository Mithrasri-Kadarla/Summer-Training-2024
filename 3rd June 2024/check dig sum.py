def dig_sum(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n=n//10
    return s
def sing_dig(n):
    while n>=10:
        n=dig_sum(n)
    return n
def chk_prime(n):
    while True:
        num=sing_dig(n)
        if num in [2,3,5,7]:
            return n
        n+=1
n=145
x=chk_prime(n)
print(x)
