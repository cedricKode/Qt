import nuke
import nukescripts.snap3d



def delTracker():
    node = nuke.thisNode()
    index = nuke.thisKnob().name()
    index = index.split('_')[1]

    track_name = 'Tracker_{}'.format(index)
    del_name = 'Delete_{}'.format(index)

    track_knob = node.knob(track_name)
    del_knob = node.knob(del_name)

    node.removeKnob(track_knob)
    node.removeKnob(del_knob)
	
		
	

def addTracker( vtx_pos ):
    #Grab this node and et index init
    node = nuke.selectedNode()
    index = node.knob('index').value()
    index = int(index)     # value return a float
    
    pos_name ="Tracker_{}".format(index)
    del_name = 'Delete_{}'.format(index)
    pos_knob = nuke.XYZ_Knob(pos_name)
    del_knob = nuke.PyScript_Knob(del_name,"Delete", "delTracker()")

    pos_knob.setAnimated()
    pos_knob.setValue( vtx_pos )         
    pos_knob.setTooltip('value')
    
    node.addKnob(pos_knob)
    node.addKnob(del_knob)
    node.knob('index').setValue(index+1)

vsel = nukescripts.snap3d.getSelection()
for v in vsel:
    tracker_list = ()
    pos = (v.position.x, v.position.y, v.position.z)
    addTracker(pos)
