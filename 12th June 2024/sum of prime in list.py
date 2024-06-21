def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

#x = [4, 8, 14, 22, 36, 68]
x=[14,16,20,22]
l = []

for i in range(1, len(x)):
    start = x[i-1]
    end = x[i]
    max_prime=0
    for j in range(end - 1, start - 1, -1):
        if is_prime(j):
            max_prime = j
            break
    if max_prime is not None:
        l.append(max_prime)
    else:
        l.append(0)
sum_of_max_primes = sum(l)
print(sum_of_max_primes)
