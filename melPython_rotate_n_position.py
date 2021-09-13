# Autodesk MAYA MEL/Python
# Rotate by N Position
# Function takes an array of integers and returns that array rotated by N positions.
# Rajesh Fithelis
# Email: rajeshf@live.com
def rightRotate(lists, num): 
    output_list = [] 
      
    # Will add values from n to the new list 
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, len(lists) - num):  
        output_list.append(lists[item]) 
          
    return output_list 
  
# Driver Code 
n = 3
list_1 = [1, 2, 3, 4, 5, 6] 
  
print(rightRotate(list_1, n)) 