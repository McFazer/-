def is_prostoe(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))
