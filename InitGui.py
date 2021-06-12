import FreeCADGui
import FCBinding

# When WB activated run Modern UI
mw = FreeCADGui.getMainWindow()
mw.workbenchActivated.connect(FCBinding.run)
