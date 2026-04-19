# greater of 2 numbers
a = 15
b = 10

def compare():
    if a > b:
        print("a is greater")
    else:
        print("b is greater")

compare()


# Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))


# Largest of 3 numbers
def largest(a, b, c):
    return max(a, b, c)

print("Largest:", largest(10, 25, 15))


# Reverse String
def reverse_string(s):
    return s[::-1]

print("Reverse:", reverse_string("Python"))


# Count Vowels
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count

print("Vowels:", count_vowels("Ajith"))


# Factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print("Factorial:", factorial(5))