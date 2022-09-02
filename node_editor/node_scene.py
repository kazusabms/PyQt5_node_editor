# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :node_scene.py
@describe    :
@time        :2022/08/15 17:01:39
@author      :touma_kazusa
@versions    :1.0
'''
from node_graphics_scene import QDMGraphoicsScene

class Scene():
    def __init__(self):
        self.nodes = []
        self.edges = []

        self.scene_wight = 64000
        self.scene_height = 64000

        self.initUI()

    def initUI(self):
        self.grScene = QDMGraphoicsScene(self)
        self.grScene.setGrScene(self.scene_wight,self.scene_height)

    def addNode(self,node):
        self.nodes.append(node)
    
    def addEdge(self,edge):
        self.edges.append(edge)
    
    def removeNode(self,node):
        self.nodes.remove(node)
    
    def removeEdge(self,edge):
        self.edges.remove(edge)
        
