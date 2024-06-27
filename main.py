from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MDLabel(text="Hello, World", halign="center")


MainApp().run()