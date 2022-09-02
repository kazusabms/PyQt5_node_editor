
# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :node_graphics_scene.py
@describe    :
@time        :2022/08/10 16:09:31
@author      :touma_kazusa
@versions    :1.0
'''
import math
import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*

class QDMGraphoicsScene(QGraphicsScene):
    def __init__ (self,scene, parent = None):
        super().__init__(parent)

        self.scene = scene

        # setting
        self.grid_size = 20
        self.grid_squares = 5 



        self._color_background = QColor("#393939")              # 给一个颜色
        self._color_light = QColor("#2f2f2f")                   # 给个亮色
        self._color_dark = QColor("#292929")                    # 给个暗色

        self._pen_light = QPen(self._color_light)               #qpen 
        self._pen_light.setWidth(1)                             #设置宽度

        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        #设置颜色为_color_background
        self.setBackgroundBrush(self._color_background)
    
    #设置场景宽高
    def setGrScene(self,width,height):
        self.setSceneRect(-width//2,-height//2,width,height)

    #使用drawBackground函数
    def drawBackground(self, painter, rect):
        super().drawBackground(painter,rect)

        #here we create our grid 
        left = int(math.floor(rect.left()))
        right =int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left-(left% self.grid_size)
        first_top = top - (top % self.grid_size)

        #compute all lines to be drawn  分布网格
        lines_light,lines_dark = [],[]
        for x in range(first_left,right,self.grid_size):
            if(x %(self.grid_size * self.grid_squares)!=0):lines_light.append(QLine(x,top,x,bottom))
            else:lines_dark.append(QLine(x,top,x,bottom))

        for y in range(first_top,bottom,self.grid_size):
            if(y %(self.grid_size * self.grid_squares)!=0):lines_light.append(QLine(left,y,right,y))
            else:lines_dark.append(QLine(left,y,right,y))
        
        # draw the lines  set笔的颜色
        painter.setPen(self._pen_light)
        painter.drawLines(*lines_light)
        
        painter.setPen(self._pen_dark)
        painter.drawLines(*lines_dark)





        # draw the

