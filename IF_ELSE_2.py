actual_cost = float(input("Enter the actual cost of the item: "))
sale_amount = float(input("Enter the sale amount: "))
if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total profit = {0}".format(amount))
else:
    print("No profit $$$")