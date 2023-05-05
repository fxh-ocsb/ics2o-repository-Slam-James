def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def Q3Primes(num1, num2):
    primes = []
    for num in range(num1, num2 + 1):
        if is_prime(num):
            primes.append(num)
    return primes

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Prime numbers between", num1, "and", num2, "are:", Q3Primes(num1, num2))