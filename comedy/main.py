from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.toast import toast
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDIcon
from kivy.properties import StringProperty, NumericProperty
Window.size = (350, 700)
import os
import cv2
KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer
BoxLayout:
    HotReloadViewer:
        size_hint_x: .10
        path: app.path_to_kv_file
        errors: True
        errors_text_color: 1, 0, 0, 1
        errors_background_color: app.theme_cls.bg_dark
'''
class ItemForCustomBottomSheet(MDCard):
    gea = StringProperty()
    
class Example(MDApp):
    ehr = 1, 1, 1, 1 
    col = '02027e'
    one = 3
    num = -1
    main = 0
    className = []
    path_to_kv_file = "new.kv"
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
        
    def change_img(self, widgets, funs):
        if self.one == 3:     
            path = 'img'
            images = []
            classNames = []
            mylist = os.listdir(path)
            for cl in mylist:
                curImg = cv2.imread(f'{path}/{cl}')
                images.append(curImg)
                classNames.append(f'{os.path.splitext(cl)[0]}{os.path.splitext(cl)[1]}')
            self.one = 60
            
            self.className = classNames
            
        if funs == 'forward': 
            if self.num >= len(self.className)-1:
               toast('ending')
            else:
                
                self.num += 1 
                widgets.source = f'img/{self.className[self.num]}'
                
                print(f'{self.className[self.num]}')
                
                
                
        elif funs == 'backward': 
            
            if self.num <= 0:
                toast('starting')
        
            else:
                self.num -= 1
                widgets.source = f'img/{self.className[self.num]}'
                print(f'{self.className[self.num]}')
            
        
        
Example().run()