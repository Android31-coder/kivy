from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

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
        
        layout = FloatLayout()
        self.score = 0

        self.lbl_title = Label(text = "Score: 0", font_size = '20sp', size_hint = (1, 0.2), pos_hint = {"top": 1})
        layout.add_widget(self.lbl_title)

        self.fish = Fish(
            size_hint = (None, None),
            size = (500, 500), 
            pos_hint = {"center_x":0.5, "center_y": 0.5}
        )

        self.fish.game_screen = self
        layout.add_widget(self.fish)
        
        back_to_menu = Button(text = "Back", font_size = '20sp', size_hint = (1, 0.15), background_color = (0.80, 0.35, 0.85, 1))
        back_to_menu.bind(on_press = self.to_menu)
        layout.add_widget(back_to_menu)
        self.add_widget(layout)

    def to_menu(self, *args):
        self.manager.current = 'menu'

    def increment_score(self, *args):
        self.score += 1
        self.lbl_title.text = f"Score: {self.score}" 

    def on_enter(self, *args):
        self.star_game()
        return super().on_enter(*args)
    
    def star_game(self):
        self.score = 0
        self.lbl_title.text = f"Score: {self.score}"
        self.fish.fish_index = 0
        self.fish.new_fish()

    def level_complete(self):
        self.lbl_title.text = "Level Complete!"

class Fish(Image):
    fish_current = None
    fish_index = 0
    hp_current = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game_screen = None

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos) or not self.opacity:
            return
        self.hp_current -= 1
        self.game_screen.score += 1
        self.game_screen.lbl_title.text = f"Score : {self.game_screen.score}"
        if self.hp_current <= 0:
            self.dead_fish()

        return super().on_touch_down(touch)

    def dead_fish(self):
        self.opacity = 0
        self.fish_index += 1
        app = App.get_running_app()
        if self.fish_index >= len(app.LEVELS[app.LEVEL]):
            self.game_screen.level_complete()
        else:
            self.new_fish()

    def new_fish(self):
        app = App.get_running_app()
        self.fish_current = app.LEVELS[app.LEVEL][self.fish_index]
        self.source = app.FISHES[self.fish_current]['source']
        self.hp_current = app.FISHES[self.fish_current]['hp']
        self.opacity = 1

class MyApp(App):
    LEVEL = 0
    FISHES = {
        "fish1":{
            "source": "assets\meme.jpg",
            "hp": 10
        },
        "fish2":{
            "source": "assets\meme1.jpg",
            "hp": 20
        },
    }
    LEVELS = [
        ["fish1", "fish2", "fish1"]
    ]
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name = 'menu'))
        sm.add_widget(Settings(name = 'Settings'))
        sm.add_widget(Game(name = 'Game'))
        return sm

my_app = MyApp()
my_app.run()
