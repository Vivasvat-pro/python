def add(p, q):
    return p + q
def substract(p, q):
    return p - q
def multiply(p, q):
    return p * q
def divide(p, q):
    return p / q
print("please select the operation")
print("a. add")
print("b. substract")
print("c. multiply")
print("d. divide")
chpice = input("Enter choice(a/b/c/d): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if chpice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))
elif chpice == 'b':
    print(num1, "-", num2, "=", substract(num1, num2))
elif chpice == 'c':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif chpice == 'd':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")and