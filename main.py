print("")
print("--------------------------")
print("Welcome to the basic calculator!")
print("Created by Mon Andrei Obillo")
print("--------------------------")
print("")

while True:
    print("Input your first value:")
    n1 = float(input())
    print("Input your second value:")
    n2 = float(input())
    print("")

    print("Choose the operation:")
    print(
        """ 
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        """
    )
    print("")
    choice = int(input("Operation: "))

    if choice in (1, 2, 3, 4):
        print("The answer is:")
    
        if choice == 1:
            print(n1, "+", n2, "=", n1 + n2)
        elif choice == 2:
            print(n1, "-", n2, "=", n1 - n2)
        elif choice == 3:
            print(n1, "x", n2, "=", n1 * n2)
        elif choice == 4:
            print(n1, "/", n2, "=", n1 / n2)
        
        print("")
        next_equation = str(input("Do you want another calculation? (yes or no) "))
        if next_equation == 'no':
            break
        elif next_equation == 'yes':
            True
        else:
            print('"yes or no only!" - creator')
            print("")
    else:
        print("Invalid input, please try again.")

print("")
print("--------------------------")
print("Thank you for using the basic calculator")
print("Credits to: Mon Andrei Obillo")
print("Copyright 2024")
print("--------------------------")
print("")
