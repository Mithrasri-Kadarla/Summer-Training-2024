
def check_palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return int(n)
    else:
        return check_palindrome(n+1)

n=int(input())
print(check_palindrome(n))
