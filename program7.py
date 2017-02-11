#PROGRAM TO ENTER 2 ANGLES AND FIND THIRD ANGLE
def thirdangle(angle1,angle2):
    v3=180-(angle1+angle2)
    print("Third angle ",v3)
v1=int(input("Enter the angle 1 "))
v2=int(input("Enter the angle 2 "))
thirdangle(v1,v2)
