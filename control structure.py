'''
#if
a=100
b=20

if a>b:
    print("a is max")

# if else
a=100
b=20



if a<b:
    print("a is max")
else:
    print("b is max")



age = int(input("Enter your age"))

if age >=18:
    print("you age is eligibal for voting")
else:
    print("you age is not eligibal for voting")
'''
'''
#ladder

a= int(input("Enter you nember a:"))
b= int(input("Enter you nember b:"))
c= int(input("Enter you nember C:"))     

if a>b and a<c:
    print("a is max")
elif b>c:
    print("b is max")
elif c>a:
    print("c is max")
    
'''
'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
'''
'''
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Neutral")
'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter an operator (+, -, *, /): ")

if op == '+':
    print(f"Result: (num1 + num2)")
elif op == '-':
    print(f"Result: (num1 - num2)")
elif op == '*':
    print(f"Result: (num1 * num2)")
else:
    print("Invalid operator")
