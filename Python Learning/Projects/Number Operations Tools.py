#Number Operations Tools ( Iteration Statements Based Project )
#(even/odd, digit sum, reverse number and palindrome)

while True:
    num = int(input("Enter Numbers:"))

    #Odd/Even
    if num % 2 == 0:
        print("This is Even Number")
    else:
        print("This is Odd Number")
    
    #Sum Digit
    temp = num
    sum=0
    while temp>0:
        digit = temp % 10
        sum += digit
        temp = temp // 10

    print("Sum Of Digit:",sum)
    
    #Reverse Number 
    temp = num
    rev = 0 
    while temp>0:
        digit=temp%10
        rev = rev * 10 + digit
        temp = temp // 10 
    print("This a Reverse Of Num",rev)

    #Palindrome
    if num == rev :
        print("Palindrome Number is ",rev)
    else:
        print("Not Palindrome Number is ",rev)  
    
    
    choice = input("Do U want Stop:(yes/no)")
    if choice == "no":
        break
'''

'''