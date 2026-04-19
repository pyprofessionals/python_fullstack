# VARIABLES 

# Variable is used to store data

x = 10
name = "Ajith"
price = 99.5

print("x:", x)
print("name:", name)
print("price:", price)

# 2. Assignment Operator (=)
# Assign value to variable

a = 20
b = 5

print("a:", a)
print("b:", b)

# Re-assign value
a = 50
print("Updated a:", a)

# 3. Relational Operators
# >, <, ==, !=, >=, <=

num1 = 10
num2 = 20

print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)
print("num1 >= num2:", num1 >= num2)
print("num1 <= num2:", num1 <= num2)


# 4. Scope of Variables
# Local and Global

# Global variables
g1 = 100
g2 = 200

def scope_example():
    # Local variable
    local_var = g1 + g2
    print("Inside function (local):", local_var)

scope_example()

print("Outside function g1:", g1)
print("Outside function g2:", g2)


# 5. Local Variable Example
def local_demo():
    x = 50   # local
    print("Local x:", x)

local_demo()

# print(x) cannot access (error)


# 6. Global Variable Example
y = 30   # global

def global_demo():
    print("Access global y:", y)

global_demo()
print("Outside y:", y)


# 7. Modify Global Variable
count = 0

def update():
    global count
    count = count + 1

update()
update()
print("Updated count:", count)

# 8. Local vs Global Same Name
z = 5   # global

def test():
    z = 10   # local
    print("Inside function z:", z)

test()
print("Outside function z:", z)
