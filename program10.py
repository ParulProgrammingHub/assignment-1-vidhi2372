#PROGRAM TO CALCULATE SIMPLE INTEREST
def simpleinterest(p,t,r):
    s=(float(p*t*r)/100)
    print("Simple interest is ",s)
p=int(input("Enter the principal amount "))
r=int(input("Enter the rate "))
t=int(input("Enter the time "))
simpleinterest(p,t,r)
