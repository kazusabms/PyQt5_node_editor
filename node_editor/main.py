# -*- encoding: utf-8 -*-
#!/usr/bin/env python
'''
@file        :main.py
@describe    :
@time        :2022/08/10 15:37:29
@author      :touma_kazusa
@versions    :1.0
'''


import sys 
from PyQt5.QtWidgets import *
from node_editor_wnd import NodeEditorWnd
# from node_graphics_scene import QDMGraphoicsScene     #导入node_graphics_scene

if __name__ =="__main__":
    app =QApplication(sys.argv)
    wnd = NodeEditorWnd()
    sys.exit(app.exec_())
