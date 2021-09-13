import maya.cmds as cmds

selected = cmds.ls(selection=True)
for item in selected:
    translate_x_value = cmds.getAttr("%s.translateX" % item)
    translate_y_value = cmds.getAttr("%s.translateY" % item)
    translate_z_value = cmds.getAttr("%s.translateZ" % item) 
    ix1, iy1, iz1, ix2, iy2, iz2 = cmds.exactWorldBoundingBox(item) 
    translate_Y = iy2-iy1
    cmds.polyCone(sx=10, sy=15, sz=10, r=0.3, h=1)
    cmds.move(translate_x_value, translate_y_value, translate_z_value)
    cmds.rotate( '180deg', 0, 0, r=True )
    x1, y1, z1, x2, y2, z2 = cmds.exactWorldBoundingBox(calculateExactly=True)
    xc = (x2 + x1) / 2.0
    yc = (y2 + y1) / 2.0
    zc = (z2 + z1) / 2.0    
    cmds.xform(worldSpace=True, pivots=[xc,y1,zc])
    
