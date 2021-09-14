# Autodesk MAYA MEL/Python
# To execute existing MEL scripts
# Rajesh Fithelis
# Email: rajeshf@live.com
import maya.mel as mel
mel.eval('source "myMainMELScript.mel"')
mel.eval('source "myMELScript2.mel"')
mel.eval('mySourcedFunction(1)')