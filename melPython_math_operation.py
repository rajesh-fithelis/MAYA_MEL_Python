# Autodesk MAYA MEL/Python
# Math Operation: Find Perpendicular 3D Point
# Write a function to find out perpendicular 3d point on any two-given point in 3d space.
# Rajesh Fithelis
# Email: rajeshf@live.com  
def perp(a1, a2, a3, b1, b2, b3) : 
    p1 = abs((a2*b3)-(a3*b2))  
    p2 = abs((a3*b1)-(a1*b3))  
    p3 = abs((a1*b2)-(a2*b1))
    print("Output:")
    print(p1,p2,p3)
  
# Code  
if __name__ == "__main__" : 
    # point A
    a1 = 1
    a2 = 0 
    a3 = 0
    # point B    
    b1 = 0 
    b2 = 0
    b3 = 1 
    # function call  
    perp(a1, a2, a3, b1, b2, b3)