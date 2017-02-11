#PROGRAM TO FIND MEAN AND % OF 5 SUBJECTS
m1=int(input("Enter the marks of subject 1 "))
m2=int(input("Enter the marks of subject 2 "))
m3=int(input("Enter the marks of subject 3 "))
m4=int(input("Enter the marks of subject 4 "))
m5=int(input("Enter the marks of subject 5 "))
mean=m1+m2+m3+m4+m5
print("Mean is ",mean)
per=mean/500*100
print("Percentage is ",per)
if per<35:
    print("FAIL")
else:
    print("PASS")
