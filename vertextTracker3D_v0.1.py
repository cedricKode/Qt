'''
Created on March 11, 2013
@author: Ryuu
    
    This python script is associated with the VextexTarcker gizmo (tdplugins/nuke/common/plugins/td/VertexTracker.gizmo).
    
'''
import nuke
import imath
import td.nuke.geo as tdGeo
import td.nuke.logger as tdLogger
import td.nuke.infos as tdInfos
import td.nuke.lib.core.graph as tdgraph
import numpy as np

#===================================
def execAction(gizmo, frame=1):
    '''
    execAction(node, frame=101):
    This function bakes position values inside the gizmo's knob 'tdVal3DPos'.
    This is based on selected vertices position into 3D space. 
    Those values corresponds to the center
    of the selected vertices bounding box.

        @param 'gizmo': Must be a Gizmo object Nuke.
        @param 'frame': Must be an integer.

    Created on March 11, 2013
    @author: Ryuu
    '''
    # |  TESTS  |-----------------------------------------
    if gizmo != None:
        if (gizmo.__class__.__name__) != 'Gizmo':
            tdLogger.printError('td.nuke.gizmos.vertexTracker3D', 'execAction()', "Argument 'node' must be a Gizmo object Nuke")
            
    if not isinstance(frame, int):
        tdLogger.printError('td.nuke.gizmos.vertexTracker3D', 'execRange()', "Argument 'frame' must be an integer")
        
    #|  VARIABLES  |---------------------------------------------------------------------------------
    positionList = list()
    transNodeKnob = gizmo.knob('tdVal3DPos')
    trans2DNodeKnob = gizmo.knob('tdVal2DPos')
    width = gizmo.width()
    height = gizmo.height()
    camera = gizmo.input(1)
    if camera.Class() not in ['Camera2']:
        camera = search_upstream(gizmo.input(1))[0]
    camera = tdGeo.Camera(camera)
        # |  EXECUTE  |-----------------------------------------------------------
    for node in tdInfos.getSelectableGeoNodes():
        if not node.Class().startswith('ReadGeo'):
            continue
        geoObject = tdGeo.Object(node)
        vertexSelection = geoObject.getVertexSelection()
        
        #print(dir(vertexSelection))
        poslist = vertexSelection.positions()
        x = [[i[0]] for i in poslist]
        y = [[i[1]] for i in poslist]
        z = [[i[2]] for i in poslist]
        
        
        data = np.concatenate((x, y, z), axis=1)
        datamean = data.mean(axis=0)

           
           
        #print data - datamean
        uu, dd, vv = np.linalg.svd(data - datamean)
        print(vv)
#         
#         centerPosition = vertexSelection.centerPosition()
#         if centerPosition is not None:
#             positionList.append(centerPosition)
# 
#     if len(positionList) != 0:
#         positionListX = [l[0] for l in positionList]
#         positionListY = [l[1] for l in positionList]
#         positionListZ = [l[2] for l in positionList]
# 
#         minMaxX = [sorted(positionListX)[0], sorted(positionListX)[-1]]
#         minMaxY = [sorted(positionListY)[0], sorted(positionListY)[-1]]
#         minMaxZ = [sorted(positionListZ)[0], sorted(positionListZ)[-1]]
# 
#         positionX = sum(minMaxX) / (len(minMaxX) * 1.0)
#         positionY = sum(minMaxY) / (len(minMaxY) * 1.0)
#         positionZ = sum(minMaxZ) / (len(minMaxZ) * 1.0)
#         
#         
#         
#         transNodeKnob.setAnimated()
#         transNodeKnob.setValueAt(positionX, frame, 0)
#         transNodeKnob.setValueAt(positionY, frame, 1)
#         transNodeKnob.setValueAt(positionZ, frame, 2)
#         
#         
#         
#         
#         # Project the 3D vector position on the camera screen space
#         point_3D = imath.V3f()
#         point_3D[0] = positionX
#         point_3D[1] = positionY
#         point_3D[2] = positionZ
#         point_2D = camera.projet_3D_points(point_3D, frame, width, height)
#         
#         trans2DNodeKnob.setAnimated()
#         trans2DNodeKnob.setValueAt(point_2D[0], frame, 0)
#         trans2DNodeKnob.setValueAt(point_2D[1], frame, 1)
        
#===================================
def execRange(gizmo=None, firstFrame=1, lastFrame=1, incrFrame=1, views=None):
    '''
    execAction(node, firstFrame=101, lastFrame=159, incrFrame=1, views=['L', 'R']):
    This function execute an action to the node with the given range and the views in argument.
        
        @param 'gizmo': Must be a Gizmo object Nuke.
        @param 'firstFrame': Must be an integer.
        @param 'lastFrame': Must be an integer.
        @param 'incrFrame': Must be an integer.
        @param 'views': Must be a string or a list of views le 'L' or 'R'.
        
    Created on March 11, 2013
    @author: Ryuu
    '''
    #|  TESTS  |-------------------------------------------------------------------------------------
    if gizmo != None:
        if (gizmo.__class__.__name__) != 'Gizmo':
            tdLogger.printError('td.nuke.gizmos.vertexTracker3D', 'execRange()', "Argument 'node' must be a Gizmo object Nuke")
            
    if not isinstance(firstFrame, int):
        tdLogger.printError('td.nuke.gizmos.vertexTracker3D', 'execRange()', "Argument 'firstFrame' must be an integer")
        
    if not isinstance(lastFrame, int):
        tdLogger.printError('td.nuke.gizmos.vertexTracker3D', 'execRange()', "Argument 'lastFrame' must be an integer")
        
    if not isinstance(incrFrame, int):
        tdLogger.printError('td.nuke.gizmos.vertexTracker3D', 'execRange()', "Argument 'incrFrame' must be an integer")
        
    if views != None:
        if (views.__class__.__name__) not in ['str', 'list']:
            tdLogger.printError('td.nuke.gizmos.vertexTracker3D', 'execRange()', "Argument 'views' must be a string or a list")
            
    #|  HACK  |--------------------------------------------------------------------------------------
    # Add a CurveTool to force the evaluation
    tempNode = nuke.nodes.CurveTool()
    
    #|  CLEAR ANIMATION  |---------------------------------------------------------------------------
    for i in xrange(firstFrame, (lastFrame+1),  incrFrame):
        nuke.root().setFrame(i)
        transNodeKnob = gizmo.knob('tdVal3DPos')
        transNodeKnob.removeKeyAt(i)
        
    #|  EXECUTE  |-----------------------------------------------------------------------------------
    for i in xrange( firstFrame, (lastFrame+1),  incrFrame):
        nuke.root().setFrame(i)
        # Execute the CurveTool to force the evaluation
        nuke.execute(tempNode, i, i, 1, views, continueOnError=True)
        # Then execute the execAction
        execAction(gizmo, i)
        
    #|  DELETE HACK  |-------------------------------------------------------------------------------
    nuke.delete(tempNode)


#====================================================================================================

def getRange(gizmo):
    '''
    getRange(node):
    This function set a range in order to execute an action to the node.
    It depends on the gizmo's knob 'tdRangeMode'. If the 'tdRangeMode' is set to 'Custom'
    it opens a pop-up window where we can set a user range before executing the action.
    Other range modes could be choose like 'Global' or 'Current'.
        
        @param 'gizmo': Must be a Gizmo object Nuke.
        
    Created on March 11, 2013
    @author: Ryuu
    '''
    #|  TESTS  |-------------------------------------------------------------------------------------
    if gizmo != None:
        if (gizmo.__class__.__name__) != 'Gizmo':
            tdLogger.printError('td.nuke.gizmos.vertexTracker3D', 'getRange()', "Argument 'node' must be a Gizmo object Nuke")
            
    #|  VARIABLES  |---------------------------------------------------------------------------------
    rangeMode = gizmo.knob('tdRangeMode').value()
    
    #|  EXECUTE  |-----------------------------------------------------------------------------------
    if rangeMode == 'Custom':
        firstFrame = nuke.root().firstFrame()
        lastFrame  = nuke.root().lastFrame()
        userInput = nuke.getFramesAndViews('Range', '%s-%s' %(firstFrame, lastFrame))
        if not userInput:
            pass
        else:
            views = userInput[1]
            if views == ['main']:
                views = ['L', 'R']
            userRange  = nuke.FrameRange(userInput[0])
            userFirstFrame = userRange.first()
            userLastFrame  = userRange.last()
            userIncrFrame  = userRange.increment()
            
            execRange(gizmo, userFirstFrame, userLastFrame, userIncrFrame, views)
            
    elif rangeMode == 'Global':
        views = nuke.views()
        firstFrame = nuke.root().firstFrame()
        lastFrame  = nuke.root().lastFrame()
        
        execRange(gizmo, firstFrame, lastFrame, 1, ['L', 'R'])
        
    elif rangeMode == 'Current':
        views = nuke.views()
        currentFrame = nuke.frame()
        
        execRange(gizmo, currentFrame, currentFrame, 1, ['L', 'R'])

def search_upstream(node, cameras=list()):
    if bool(node.maxInputs()):
        dnodes = tdgraph.get_depnodes(node, 'up')
        for dnode in dnodes:
            if dnode.Class() in ['Camera2']:
                cameras.append(dnode)
                break
            else:
                search_upstream(dnode, cameras)
    return cameras
    
    
