'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        minimum = a
    else:
        minimum = c
else:
    if b < c:
        minimum = b
    else:
        minimum = c

print("Minimum number is:", minimum)        
'''
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:
    if a > c:
        if a > d:
            maximum = a
        else:
            maximum = d
    elif c > d:
        maximum = c
    else:
        maximum = d
else:
    if b > c:
        if b > d:
            maximum = b
        else:
            maximum = d
    elif c > d:
        maximum = c
    else:
        maximum = d

print("Maximum number is:", maximum)
'''
'''
n = int(input("Enter a number: "))


print("Positive" if n > 0 else "Non-Positive")
'''
'''
marks = int(input("Enter marks: "))


print("Pass" if marks >= 40 else "Fail")
'''
'''
num = int(input("Enter a number: "))


print("Even" if num % 2 == 0 else "Odd")
'''
