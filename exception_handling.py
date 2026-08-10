try:
    num1,num2 = eval(input("enter two numbers, separated by a coma:"))
    result = num1 / num2
    print("result is ",result)
except ZeroDivisionError:
    print("Error: Division by zero is error.")
except SyntaxError:
    print("Error: Invalid input. Please enter two numbers separated by a comma.")
except:
    print("wrong input")
else:
    print("no excpetion")
finally:
    print("this will execute no matter what")