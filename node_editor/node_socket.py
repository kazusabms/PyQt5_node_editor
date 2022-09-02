# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :node_scene.py
@describe    :
@time        :2022/08/15 17:01:39
@author      :touma_kazusa
@versions    :1.0
'''

#节点的接口相关设置
from node_graphics_socket import QDMGraphicsSocket

LEFT_TOP = 1
LEFT_BOTTOM =2 
RIGHT_TOP=3
RIGHT_BOTTOM =4

class Socket():
    def __init__(self,node,index = 0, position = LEFT_TOP):

        self.node = node
        self.index = index
        self.position = LEFT_TOP

        self.grSocket = QDMGraphicsSocket(self.node.grNode)
        self.grSocket.setPos(*self.node.getSocketPosition(index,position))

