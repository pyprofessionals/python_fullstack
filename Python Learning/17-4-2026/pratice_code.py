#Quiz Pratice Of Print Statement & Variables

'''
1. print("10+5",end=" ")
   print(10+5)
desired sentence : 2+3=5

'''
#Answer
print("2+3",end="=")
print(2+3)

'''
2. print("hi","hi",sep=" ",end=" ")
   print("hi")
   you have to print "hi...hi...hi"
'''
#Answer
print("hi","hi",sep="...",end="...")
print("hi")

'''
3. find the output of below code
   name="Yuvaraj"
   crop="Rice"
   yield=100
   print(yield)
'''
#Answer - SyntaxError

'''
4. find the datatype of below variables
   a="100.0"

'''
#Answer
a="100.0"
print(type(a))      # printing the datatype of a

'''
5. How to change the datatype of a variable?
    a=10
    print(type(a))
    change the datatype of a to string and print the type of a
'''
#Answer
a=10
print(type(a))      
a=str(a)           # changing the datatype of a to string
print(type(a))      # printing the type of a after changing the datatype

'''
5. Create a variable name "name" and assign your name to it and print the variable
Name
Age
Available_for_work
Rating
'''
#Answer
name="Harish"  #String variable
age=21        #Integer variable
available_for_work=True  #Boolean variable
rating=4.5    #Float variable

'''
6. Is Python have Char datatype?
'''
#Answer - No, Python does not have a Char datatype.

'''
7. What is the output of below code
   a=10     
   b=20
   print(a+b) 
   print(a-b)
   print(a*b)       
   print(a/b) 

'''
#Answer - 30  -10  200  0.5