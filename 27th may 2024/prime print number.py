def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_next_prime(number):
    next_number = number + 1
    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1

input_number = int(input("Enter a number: "))
if is_prime(input_number):
    print(input_number)
else:
    next_prime = find_next_prime(input_number)
    print(next_prime)
'''
n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
            break
        if c==0:
            print(n)
            break
        else:
            n+=1
            
'''
