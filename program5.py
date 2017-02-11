#PROGRAM TO ENTER VALUE IN DAYS AND CONVERT IN YEARS MONTHS AND DAYS
d=int(input("Enter the value in days "))
y=int(d/365)
d=d%365
m=int(d/30)
d=d%30
print("years ",y)
print("Months",m)
print("Day",d)
