# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :node_scene.py
@describe    :
@time        :2022/08/15 17:01:39
@author      :touma_kazusa
@versions    :1.0
'''
from node_graphics_node import QDMGraphicsNode
from node_content_widget import QDMNodeContentWidget
from node_socket import *

class Node():
    def __init__(self,scene,title="Underfined Node",inputs=[],outputs=[]):
        self.scene = scene 

        self.title = title
        
        self.content = QDMNodeContentWidget()
        self.grNode = QDMGraphicsNode(self)
        
        
        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        #接口间隙
        self.socket_spacing=22

        #create socket for inputs and outputs  
        self.inputs = []
        self.outputs=[]
        counter = 0 
        for item in inputs:
            socket = Socket(node=self, index = counter,position = LEFT_BOTTOM)
            counter += 1
            self.inputs.append(socket)
        for item in outputs:
            socket = Socket(node=self,index=counter,position=RIGHT_TOP)
            counter += 1
            self.outputs.append(socket)

    #get 接口的位置
    def getSocketPosition(self,index,position):
        x =0  if(position in(LEFT_TOP,LEFT_BOTTOM)) else self.grNode.width

        if position in(LEFT_BOTTOM,RIGHT_BOTTOM):
             # start from bottom  从底部开始
            y = self.grNode.height - self.grNode.edge_size -self.grNode._padding - index * self.socket_spacing
        else:
            # start from top  从顶部开始
            y = self.grNode.title_height + self.grNode._padding + self.grNode.edge_size + index*self.socket_spacing

        return x,y