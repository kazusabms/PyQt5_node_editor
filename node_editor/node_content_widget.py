from lib2to3.pytree import Node
from PyQt5.QtWidgets import * 

class QDMNodeContentWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.initUI()
    
    #创建节点内容
    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        self.wdg_label = QLabel('Some Title')
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QTextEdit('foo'))
