import maya.cmds as cmds
import maya.mel as mel
import sys


transforms = cmds.ls(tr=True)
polyMeshes = cmds.filterExpand(transforms, sm=12)
cmds.select(polyMeshes, r=True)
#NEW2 
#cmds.delete()

probuilderPath = 'D:\ProBuilder\ProBuilder'
if probuilderPath not in sys.path:
    sys.path.append(probuilderPath)


if globals().has_key('init_modules'):
	for m in [x for x in sys.modules.keys() if x not in init_modules]:
		del(sys.modules[m]) 
else:
	init_modules = sys.modules.keys()
	

init_modules = sys.modules.keys()

import ProBuilder


