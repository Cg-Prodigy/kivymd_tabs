from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase

class TabsUI(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def reveal_buttons(self):
        print('Working')
