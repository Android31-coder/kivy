from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Window.size = (1200, 700)

class Menu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation = 'vertical', padding = '20dp', spacing = '20dp')

        lbl_title = Label(text = "Main Menu", font_size = '40sp', size_hint = (1, 0.2))
        layout.add_widget(lbl_title)

        btn_play = Button(text = 'PLAY', size_hint = (1, 0.15), font_size = '20sp', background_color = 'red')
        layout.add_widget(btn_play)

        self.add_widget(layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name = 'menu'))
        return sm

my_app = MyApp()
my_app.run()