# FUNCTIONS 

# 1. Parameters vs Arguments
def add(a, b):   # parameters
    print("Addition:", a + b)

add(10, 20)      # arguments
add("Ajith ", "Varma")

# 2. Function Types

# (1) No arguments, No return
def message():
    print("Welcome to Python")

message()


# (2) With arguments, No return
def greet(name):
    print("Hello " + name)

greet("Ajith")


# (3) No arguments, With return
def get_number():
    return 100

num = get_number()
print("Returned number:", num)


# (4) With arguments, With return
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication:", result)


# 3. Types of Arguments

# Positional
def student(name, age):
    print("Student:", name, age)

student("Ajith", 21)


# Keyword
student(age=21, name="Ajith")


# Default
def country(name="India"):
    print("Country:", name)

country()
country("USA")


# 4. Built-in Functions
print("Length:", len([1,2,3,4]))
print("Type:", type(10))
print("Max:", max(10, 20, 30))
print("Min:", min(10, 20, 30))
print("Sum:", sum([1,2,3,4]))

# input function (uncomment to use)
# name = input("Enter your name: ")
# print("Your name is:", name)

# 5. User Defined Function
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))

# 6. Real Example (Area)
def area(length, width):
    return length * width

print("Area:", area(5, 10))

# 7. Multiple Return Values
def calc(a, b):
    return a+b, a-b

x, y = calc(10, 5)
print("Addition:", x)
print("Subtraction:", y)

# 8. Function with List
def total(lst):
    return sum(lst)

print("Total:", total([1,2,3,4]))


