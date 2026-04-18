#identifier
'''
The Name used to identify a variable is called an identifier.
'''
x=10  #x is variable and 10 is value
print(x) #printing the value of x

#identifier rules

#Rule1
'''
yield="hello"
print(yield)
#Keywords cannot be used as identifiers
'''

#Rule2
A=20
a=30
#Python is case sensitive language, so A and a are different variables
print(A,a)

#Rule3
#1name="Yuvaraj"
name1="Yuvaraj"
print(name1) #Variable name cannot start with integer

#Rule4
print_statement_="Hello, World!"
print(print_statement_) #we can use underscrore in front,end,mid 

#Dynamic Typing
b=20
print(b)
b=30
print(b)

#Data Types
'''
int - simple data type Ex: 9
float - simple data type Ex: 9.5
str - simple data type Ex: "Hello"
bool - simple data type Ex: True/False

tuple - complex data type Ex: (1,2,3)    
list - complex data type Ex: [1,2,3]
set - complex data type Ex: {1,2,3}
dict - complex data type Ex: {"name":"Yuvaraj","age":25}

'''
# How to check the data type of a variable?
age=25.3
print(type(age))