age = int(input("Enter your age: "))

if age < 0:
    print("wrong age aage cannot be negative.")
elif age > 130:
    print("wrong age please enter a real age.")
else:
    print("Your age is valid.")

    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")

if ValueError:
    print("Error please enter a correct number.")
else:
    print("Thank you for providing your age.")
