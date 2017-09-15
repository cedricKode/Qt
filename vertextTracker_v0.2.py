
import nuke
import nukescripts.snap3d
# 
# 
def indxInit():
     node = nuke.thisNode()
     node.knob('index').setValue(0)
 
 
 
 
 
def delTracker():
    node = nuke.thisNode()
    index = nuke.thisKnob().name()
    index = index.split('_')[1]

    tracker3d_name = 'Tracker_{}'.format(index)
    del_name = 'Delete_{}'.format(index)

    track3d_knob = node.knob(tracker3d_name)
    del_knob = node.knob(del_name)

    node.removeKnob(track3d_knob)
    node.removeKnob(del_knob)
            
               
 
def addTracker( vtx_pos ):
    node = nuke.thisNode()
    index = node.knob('index').value()
    index = int(index)      #value return a float
    
    pos_name ="Tracker_{}".format(index)
    del_name = 'Delete_{}'.format(index)
    pos3d_knob = nuke.XYZ_Knob(pos_name)
    del_knob = nuke.PyScript_Knob(del_name,"Delete", "delTracker()")

    pos3d_knob.setAnimated()
    pos3d_knob.setValue( vtx_pos )         
    pos3d_knob.setTooltip('value')
    
    node.addKnob(pos3d_knob)
    node.addKnob(del_knob)
    node.knob('index').setValue(index+1)

vsel = nukescripts.snap3d.getSelection()



#averNorm = nukescripts.snap3d.averageNormal(vsel) # Return a _nukemath.Vector3 which is the average of the normals of all selected point
#averPos = nukescripts.snap3d.calcAveragePosition(vsel) # Calculate the average position of all points.
#averPos = nukescripts.snap3d.calcBounds(vsel) # Calculate the average position of all points.



# vsel = (nukescripts.snap3d.getSelection())
# 
# hlp = help(ns3)
# 
# vsel = nukescripts.snap3d.allNodes()
# 
# 
# arvNorm = ns3.averageNormal(vsel)
# 
# rotationVec = ns3.calcRotationVector(vsel,arvNorm)




for v in vsel:
    tracker_list = ()
    vtx_pos = (v.position.x, v.position.y, v.position.z)
    
    
    addTracker(vtx_pos)


#https://en.wikipedia.org/wiki/Transformation_matrix
