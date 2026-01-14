from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Window.size = (1200, 700)
Window.clearcolor = (0.25, 0.14, 0.26, 1)

class Menu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation = 'vertical', padding = '20dp', spacing = '20dp')

        lbl_title = Label(text = "Main Menu", font_size = '40sp', size_hint = (1, 0.2))
        layout.add_widget(lbl_title)

        btn_play = Button(text = 'PLAY', size_hint = (1, 0.15), font_size = '20sp', background_color = (0.80, 0.35, 0.85, 1))
        layout.add_widget(btn_play)

        btn_play.bind(on_press = self.go_game)

        btn_settings = Button(text = 'Settings', size_hint = (1, 0.15), font_size = '20sp', background_color = (0.70, 0.35, 0.85, 1))
        layout.add_widget(btn_settings)

        btn_settings.bind(on_press = self.go_settings)

        btn_exit = Button(text = 'Exit', size_hint = (1, 0.15), font_size = '20sp', background_color = (0.60, 0.35, 0.85, 1))
        btn_exit.bind(on_press=lambda x: App.get_running_app().stop())
        layout.add_widget(btn_exit)

        self.add_widget(layout)

    def go_game(self, *args):
        self.manager.current = 'Game'

    def go_settings(self, *args):
        self.manager.current = 'Settings'

class Settings(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        layout = BoxLayout(
            orientation = 'vertical',
            padding = '20dp',
            spacing = '20dp'
        )
        lbl_title = Label(text = "Settings", font_size = '20sp', size_hint = (1, 0.2))
        layout.add_widget(lbl_title)
        
        back_to_menu = Button(text = "Back", font_size = '20sp', size_hint = (1, 0.15), background_color = (0.80, 0.35, 0.85, 1))
        back_to_menu.bind(on_press = self.to_menu)
        layout.add_widget(back_to_menu)
        self.add_widget(layout)

    def to_menu(self, *args):
        self.manager.current = 'menu'

class Game(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        layout = BoxLayout(
            orientation = 'vertical',
            padding = '20dp',
            spacing = '20dp'
        )
        self.score = 0

        self.lbl_title = Label(text = "Score: 0", font_size = '20sp', size_hint = (1, 0.2))
        layout.add_widget(self.lbl_title)

        btn_click = Button(text = 'Click', size_hint = (1, 0.5), font_size = '40sp')
        btn_click.bind(on_press = self.increment_score)
        layout.add_widget(btn_click)
        
        back_to_menu = Button(text = "Back", font_size = '20sp', size_hint = (1, 0.15), background_color = (0.80, 0.35, 0.85, 1))
        back_to_menu.bind(on_press = self.to_menu)
        layout.add_widget(back_to_menu)
        self.add_widget(layout)

    def to_menu(self, *args):
        self.manager.current = 'menu'

    def increment_score(self, *args):
        self.score += 1
        self.lbl_title.text = f"Score: {self.score}" 

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name = 'menu'))
        sm.add_widget(Settings(name = 'Settings'))
        sm.add_widget(Game(name = 'Game'))
        return sm

my_app = MyApp()
my_app.run()
