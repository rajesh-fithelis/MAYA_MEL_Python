# Autodesk MAYA MEL/Python
# Select object with equal vertex count
# Script to select object with equal vertex count based on the user input from current selection
# Rajesh Fithelis
# Email: rajeshf@live.com  
import maya.cmds as cmds
import functools 
import sys
import itertools

def searchVertex (*pArgs):
    number = cmds.intField(num, q=1, v=1)
    print(number)
    for eachSel in selected:
        print(eachSel)
        # query the number of vertices and faces
        ver = cmds.polyEvaluate(eachSel, v=True )
        print(ver)
        if number == ver:
            print("Vertex Matches")
        else:
            cmds.select(eachSel, d=True )
            print("Vertex Not Matched")
    print 'Search button pressed!'
            
def cancelCallback (*pArgs):
    if cmds.window (winID, exists = True):
        cmds.deleteUI (winID)
    
# Define an id string for the window first
winID = 'Test-5'

# Test to make sure that the UI isn't already active
if cmds.window(winID, exists=True):
    cmds.deleteUI(winID)
    
# selected = cmds.ls(selection=True)
cmds.select( all=True )
selected = cmds.ls(sl=True,long=True) or []

if(len(selected)>=1):
    window = cmds.window(winID, t = "TEST-5",  resizeToFitChildren=True, sizeable=False)
    cmds.rowColumnLayout (numberOfColumns = 2, columnWidth =[(1, 100), (2, 75)], columnOffset =[(1, 'left', 10)])
    cmds.separator (h = 15, style = 'none')
    cmds.separator (h = 15, style = 'none')
         
    cmds.text (label = 'Vertex Count: ')
    num = cmds.intField()
  
    cmds.separator (h = 5, style = 'none')
    cmds.separator (h = 5, style = 'none')
    cmds.text (label = '')
    cmds.button (label = 'Search', command = functools.partial (searchVertex, selected))
else:
     cmds.error('Please Create some Polygon Primitives!')  
      
cmds.showWindow(window)