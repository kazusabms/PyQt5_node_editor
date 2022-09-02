# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :node_scene.py
@describe    :
@time        :2022/08/15 17:01:39
@author      :touma_kazusa
@versions    :1.0
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QDMGraphicsSocket(QGraphicsItem):
    def __init__(self,parent = None):
        super().__init__(parent)

        #基础单位设置， 半径，宽度
        self.radius = 6.0  
        self.outline_width = 1.0 
        #设置颜色
        self._color_background = QColor('#FFFF7700')
        self._color_outline = QColor("#FF000000")

        #设置笔的颜色 宽度
        self._pen = QPen(self._color_outline)
        self._pen.setWidth(self.outline_width)
        self._brush = QBrush(self._color_background) 

    #设置画的线
    def paint(self,painter,QStyleOptionGraphicsItem,widget=None):
        #painting circle 

        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(-self.radius,-self.radius,2*self.radius,2*self.radius)

    #设置边框
    def boundingRect(self):
        return QRectF(
                - self.radius - self.outline_width,
                - self.radius - self.outline_width,
                2 * (self.radius + self.outline_width),
                2 * (self.radius + self.outline_width),
        )