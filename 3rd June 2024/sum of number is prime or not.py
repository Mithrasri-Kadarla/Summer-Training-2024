def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_digits(n):
    if n < 10:
        return m
    else:
        x = 0
        while n:
            x += n % 10
            n = n // 10
    return x

def find_prime_sum(n):
    while True:
        n = sum_digits(n)
        if n < 10:
            if is_prime(n):
                return m
            else:
                m+=1
                find_prime_sum(m)

n = int(input("Enter a number: "))
m=n
result = find_prime_sum(n)
print("The prime sum is:", result)
