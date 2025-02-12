age=int(input("plz enter your age : "))
if age<=10:
    price=5
elif age>10 and age<=20:
    price=10
elif age>20 and age<=30:
    price=15
elif age>30:
    price=20
print('the ticket price is '+str(price)+"$")
