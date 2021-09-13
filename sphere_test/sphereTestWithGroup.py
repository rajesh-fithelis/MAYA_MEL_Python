#SphereTest
import maya.cmds as cmds
import functools 
import sys

# Define an id string for the window first
winID = 'sphereTestUI'

# Test to make sure that the UI isn't already active
if cmds.window(winID, exists=True):
    cmds.deleteUI(winID)
    
selected = cmds.ls(selection=True)
if(len(selected)>1):
    cmds.error('Please select one camera!')
if(len(selected)<1):
    cmds.error('Please select anyone camera to proceed!')
selectedCamera = selected[-1]
print(selectedCamera)
currentCamera_x_value = cmds.getAttr("%s.translateX" % selectedCamera)
currentCamera_y_value = cmds.getAttr("%s.translateY" % selectedCamera)
currentCamera_z_value = cmds.getAttr("%s.translateZ" % selectedCamera) 
grp = cmds.group(empty=True, name='sphereGroup')
if(cmds.ls(type='camera')):
    window = cmds.window(winID, t = "SPHERE TEST PLUGIN",  resizeToFitChildren=True, sizeable=False)
    cmds.rowColumnLayout (numberOfColumns = 2, columnWidth =[(1, 100), (2, 75)], columnOffset =[(1, 'left', 10)]) 
    cmds.text (label = 'Sphere in (X)')
    iField = cmds.intField (value = 10, editable = True)

    cmds.text (label = 'Sphere in (Y):')
    jField = cmds.intField (value = 3, editable = True)

    cmds.text (label = 'Sphere in (Z):')
    kField = cmds.intField (value = 5, editable = True)

    cmds.text (label = 'Sphere Spacing:')
    sphereSpacingField = cmds.intField (value = 5, editable = True)

    cmds.text (label = 'Sphere Size')
    sphereSizeField = cmds.floatField (value = 1.5, editable = True)

    cmds.text (label = 'Camera Distance')
    cameraDistanceField = cmds.intField (value = 10, editable = True)
    
    cmds.separator (h = 10, style = 'none')
    cmds.separator (h = 10, style = 'none')
    
    def applyCallback (iField, jField, kField, sphereSpacingField, sphereSizeField, cameraDistanceField, *pArgs):
        print 'Generate button pressed!'
        iField = cmds.intField (iField, query = True, value = True)
        jField = cmds.intField (jField, query = True, value = True) 
        kField = cmds.intField (kField, query = True, value = True)
        sphereSpacing = cmds.intField (sphereSpacingField, query = True, value = True)
        sphereSize = cmds.floatField (sphereSizeField, query = True, value = True)
        cameraDistance = cmds.intField (cameraDistanceField, query = True, value = True)        

        count = 0
        x = (currentCamera_x_value-(iField*sphereSpacing))/2
        y = 0
        z = currentCamera_z_value-cameraDistance
        #cmds.polySphere( name = 'sphere', sx=10, sy=15, r=1 )
        #cmds.move( currentCamera_x_value, currentCamera_y_value, currentCamera_z_value )        
        for k in range(kField):
            for j in range(jField):
                for i in range(iField):
                    count += 1
                    nam = 'sphere' + str(count)
                    cmds.polySphere( name = nam, sx=10, sy=15, r=sphereSize )
                    x += sphereSpacing
                    y += 0
                    cmds.move( x, y, z )
                    cmds.parent(nam, grp)
                y += sphereSpacing          
                x = (currentCamera_x_value-(iField*sphereSpacing))/2
            z -= sphereSpacing
            y = 0        
         
    cmds.button (label = 'Generate', command = functools.partial (applyCallback, iField, jField, kField, sphereSpacingField, sphereSizeField, cameraDistanceField)) 
    def cancelCallback (*pArgs):
        if cmds.window (winID, exists = True):
            cmds.deleteUI (winID)
    cmds.button (label = 'Cancel', command = cancelCallback)
    

cmds.showWindow(window)