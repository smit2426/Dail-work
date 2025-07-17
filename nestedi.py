
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()


for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end=' ')
    print()


for i in range(1, 6):
    for j in range(i, 6):
        print(j, end=' ')
    print()

for i in range(1, 6):
    for j in range(6 - i):
        print(i, end=' ')
    print()    


for i in range(5, 0, -1):
    for j in range(i):
        print((j + 1) % 2, end=' ')
    print()


for i in range(65, 70):
    for j in range(i, 64, -1):
        print(chr(j), end=' ')
    print()

num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()
