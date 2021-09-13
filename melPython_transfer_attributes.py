# Autodesk MAYA MEL/Python
# Transfer all attributes
# Script to transfer all attributes values from first selected object to secondly selected object. 
# List all attribute and apply all attribute value on second object.
# Also check that both should be same type of objects.
# Rajesh Fithelis
# Email: rajeshf@live.com  
import maya.cmds as cmds
import functools 
import sys
import itertools

selected = cmds.ls(sl=True,long=True) or []
if(len(selected)==2):
    print("Two objects selected!")
    x=1
    for eachSel in selected:
        if x==1:
            object1 = eachSel
        else:
            object2 = eachSel
            if cmds.objectType( object2, isType=cmds.objectType(object1)):
                print("Both objects are equal")
                cmds.copyAttr(object1,object2,inConnections=True,values=True)
                print("Artibuttes copied successfully")
            else:
                print ("Something went wrong! check the number of selected objects!")            
        x=x+1
    
else:
    print("Something went wrong! check the number of selected objects!")