name = input("Enter name: ")

print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

choice = input("Enter choice : ")

while choice != 'Q':
    if choice == 'H':
        print("Hello",name)
        choice = input("Enter choice : ")
    elif choice == 'G':
        print("Goodbye",name)
        choice = input("Enter choice : ")
    else:
        print("Invalid Choice")
        choice = input("Enter choice : ")

print("Finished")