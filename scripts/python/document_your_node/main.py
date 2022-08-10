from PySide2 import QtGui,QtCore,QtWidgets,QtUiTools
import hou
import os

ui_file_main = os.path.join(os.path.dirname(__file__),'ui',"document_your_node_ui.ui")
class MainWidgets(QtWidgets.QWidget):
    
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        # load ui file
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_file_main,parentWidget=self)
        self.resize(800,1000)
        self.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)

    def closeEvent(self, event):
        self.setParent(None)

    def resizeEvent(self,event):
        self.resize(event.size())
        event.accept()
    

def show():
    dialog = MainWidgets()
    dialog.show()
    return dialog

if __name__ == "__main__":
    show()