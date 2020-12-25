
#defining functions for operations

def add(x,y):       #addition
    temp = x+y
    print(temp)

def sub(x,y):       #subtraction
    temp = x-y
    print(temp)

def mul(x,y):       #multipication
    temp = x*y
    print(temp)

def div(x,y):       #division
    temp = x/y
    print(temp)

#declaring a variable for continuity
con = 'y'

#Entering into While loop
while (con == 'y'):

    #getting input from user
    x = int(input("Enter the first number : "))     
    y = int(input("Enter the second number : "))
    op = input("Enter the operation you want to perform (+,-,x,/) : ")

    #conditions to perform the operation
    if (op=='+'):
        add(x,y)

    elif (op=='-'):
        sub(x,y)

    elif (op=='x' or op=='*'):
        mul(x,y)

    elif (op=='/'):
        if(y != 0):     
            div(x,y)
        else:       #handling division by zero
            print("Error cannot divide by 0")

    #in case user inputs other operation
    else:
        print("Invalid Input")

    con = input("Do you want to continue ? ")