#PROGRAM TO FIND COMPOUND INTEREST
def compound_interest (p,t,r):
    c=float(p*((1+r)**t)-p)
    print("Compound interest is ",c)
p=float(input("Enter the principal amount "))
r=float(input("Enter the rate "))
r=r/100
t=int(input("Enter the time "))
compound_interest(p,t,r)
