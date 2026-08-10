try:
    number = int(input("Please enter a number: "))
    print("You entered: number")
except ValueError as ex:
    print("exeption:", ex)