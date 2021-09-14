# Autodesk MAYA MEL/Python
# Open a Maya file, assign the default shader to all meshes, and save the scene.
# Rajesh Fithelis
# Email: rajeshf@live.com
import maya.standalone
import maya.cmds as cmds
  
def assign_default_shader(file_path):
    # Start Maya in batch mode
    maya.standalone.initialize(name='python')

    # Open the file with the file command
    cmds.file(file_path, force=True, open=True)

    # Get all meshes in the scene
    meshes = cmds.ls(type="mesh", long=True)
    for mesh in meshes:
        # Assign the default shader to the mesh by adding the mesh to the
        # default shader set.
        cmds.sets(mesh, edit=True, forceElement='initialShadingGroup')

    # Save the file       
    cmds.file(save=True, force=True)

    # Starting Maya 2016, we have to call uninitialize to properly shutdown
    if float(cmds.about(v=True)) >= 2019.0:
        maya.standalone.uninitialize()