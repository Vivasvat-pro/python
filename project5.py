hi = int(input("enter the amount paid by customer:"))
bye = int(input("enter the amount of bill:"))
if hi>bye:
    print("the change to be returned is:",hi-bye)
else:
    print("the customer has to pay more money")