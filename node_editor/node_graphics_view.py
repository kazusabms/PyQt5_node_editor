# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :node_scene.py
@describe    :
@time        :2022/08/15 17:01:39
@author      :touma_kazusa
@versions    :1.0
'''
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*

class QDMGraphicsView(QGraphicsView):
    def __init__(self,grScene,parent = None):
        super().__init__(parent)
        self.grScene = grScene
        self.initUI()
        self.setScene(self.grScene)

        self.zoomInFactor = 1.25
        self.zoom = 10
        self.zoomStep = 1
        self.zoomRange = [0,10]

    def initUI(self):
        #防止图形走样
        self.setRenderHints(QPainter.Antialiasing|QPainter.HighQualityAntialiasing|QPainter.TextAntialiasing|
        QPainter.SmoothPixmapTransform)

        #更新viewmode
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)   
        #取消左右滑轮显示  
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    #鼠标下压事件
    def mousePressEvent(self, event):
        #判断中键下压
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() ==Qt.LeftButton:
            self.LeftMouseButtonPress(event)
        elif event.button() ==Qt.RightButton:
            self.RightMouseButtonPress(event)
        
        else:
            super().mousePressEvent(event)
    
    #鼠标释放事件
    def mouseReleaseEvent(self, event):
        #判断中键下压
        if event.button()==Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() ==Qt.LeftButton:
            self.LeftMouseButtonRelease(event)
        elif event.button() ==Qt.RightButton:
            self.RightMouseButtonRelease(event)
        else:
            super().mouseReleaseEvent(event)
    
    #下压释放函数，中键下压执行拖拽功能
    def middleMouseButtonPress(self,event):
        print("press Released")
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease,event.localPos(),event.screenPos(),
                                Qt.LeftButton,Qt.NoButton,event.modifiers())
        super().mouseReleaseEvent(releaseEvent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        fakeEvent =QMouseEvent(event.type(),event.localPos(),event.screenPos(),
                        Qt.LeftButton,event.buttons()|Qt.LeftButton,event.modifiers())
        super().mousePressEvent(fakeEvent)
   
    def LeftMouseButtonPress(self,event):
        print("left press")
        return super().mousePressEvent(event)
    def RightMouseButtonPress(self,event):
        print("right press")
        return super().mousePressEvent(event)
    
    
    #释放触发函数
    #中键释放拖拽停止
    def middleMouseButtonRelease(self,event):
        print("MMB Released")
        fakeEvent =QMouseEvent(event.type(),event.localPos(),event.screenPos(),
                                Qt.LeftButton,event.buttons()& ~Qt.LeftButton,event.modifiers()) 
        super().mouseReleaseEvent(fakeEvent)
        self.setDragMode(QGraphicsView.NoDrag)


    
    def LeftMouseButtonRelease(self,event):
        print("left Released")
        return super().mousePressEvent(event)
    def RightMouseButtonRelease(self,event):
        print("right Released")
        return super().mousePressEvent(event)

    #滚轮缩放
    def wheelEvent(self, event):
        #计算缩放系数
        zoomOutFactor = 1/self.zoomInFactor

        if event.angleDelta().y()>0:
            zoomFator = self.zoomInFactor
            self.zoom +=self.zoomStep
        else:
            zoomFator = zoomOutFactor
            self.zoom -= self.zoomStep

        self.scale(zoomFator,zoomFator)
        return super().wheelEvent(event)


        