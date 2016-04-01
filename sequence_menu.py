a = int(input("enter first number:"))
b = int(input("enter second number:"))

print("Press 1 for  printing  even number between ", a, "and", b)
print("Press 2 for  printing odd number between ", a, "and", b)
print("Press 3 for  printing square of number between ", a, "and", b)
print("press 4 for exit")

choice = int(input("please enter choice:"))

while choice != 4:
    if choice == 1:
        if a % 2 == 0:
            for i in range(a, b + 1, 2):
                print(i, end=' ')
        else:
            for i in range(a + 1, b + 1, 2):
                print(i, end=' ')

    elif choice == 2:
        if a % 2 == 0:
            for i in range(a + 1, b + 1, 2):
                print(i, end=' ')
        else:
            for i in range(a, b + 1, 2):
                print(i, end=' ')

    elif choice == 3:
        for i in range(a, b + 1):
            print(i * i, end=' ')
    choice = int(input("please enter choice:"))
