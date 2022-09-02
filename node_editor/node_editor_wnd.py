
# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :node_editor_wnd.py
@describe    :
@time        :2022/09/02 17:31:25
@author      :touma_kazusa
@versions    :1.0
'''

import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*


from node_graphics_scene import QDMGraphoicsScene        #导入node_graphics_scene
from node_graphics_view import QDMGraphicsView
from node_scene import Scene
from node_node import Node
from node_socket import Socket


class NodeEditorWnd(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.stylesheet_filename = 'qss/nodestyle.qss'
        self.loadStylesheet(self.stylesheet_filename)


        self.initUI()
        
    
    def initUI(self):
        self.setGeometry(200,200,800,600)

        self.layout =QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)   # 布局没有边框
        self.setLayout(self.layout)


        # create graphics scene
        # self.grScene = QDMGraphoicsScene()    
        # # 调用node_scene的Scene模块，scene 功能单独写，减少代码臃肿    
        self.scene = Scene() 
        # self.grScene = self.scene.grScene

        node = Node(self.scene,'My Awesome Node',inputs=[1,2,3],outputs=[1])

        #create graphics view 
        self.view = QDMGraphicsView(self.scene.grScene,self)
        self.layout.addWidget(self.view)


        self.setWindowTitle('Node Editor')
        print("Open Node Editor")
        self.show()
        
        
        
        # self.addDebugContent()
    def addDebugContent(self):
        #创建一个绿色的画布，一个黑色的笔，设置笔的宽度为2
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        #添加一个黑色包边绿色的图标
        rect = self.grScene.addRect(-100,-100,80,100,outlinePen,greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        #添加一个text
        text = self.grScene.addText("This is my  Awesome text!",QFont("Ubuntu"))
        text.setFlag(QGraphicsItem.ItemIsSelectable)
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0,1.0,1.0))

        #添加一个名为hello world 的button
        widget1 = QPushButton("hello world")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.ItemIsMovable)
        proxy1.setPos(0,60)

        #画一条黑线
        line = self.grScene.addLine(-200,-200,400,-100,outlinePen)
        line.setFlag(QGraphicsItem.ItemIsMovable)
        line.setFlag(QGraphicsItem.ItemIsSelectable)
    
    #加载qss文件当button
    def loadStylesheet(self,filename):
        print('STYLE Loading: ',filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        QApplication.instance().setStyleSheet(str(stylesheet,encoding='uff-8'))



# if __name__ =="__main__":
#     app =QApplication(sys.argv)
#     wnd = NodeEditorWnd()
#     sys.exit(app.exec_())

