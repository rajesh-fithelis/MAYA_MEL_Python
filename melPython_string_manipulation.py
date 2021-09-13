# Autodesk MAYA MEL/Python
# String Manipulation: Find Parentheses
# Function to check parentheses paring (1{}1,101,1[]') in any given string
# Rajesh Fithelis
# Email: rajeshf@live.com  
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "False"
    if len(stack) == 0: 
        return "True"
  
# Driver code 
string = "{this [is (a) python] <test 3>}"
print("String-1: ", check(string)) 
  
string = "{this [is (a] python) <test 3>}"
print("String-2: ", check(string))  