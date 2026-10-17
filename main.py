from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        return Label(text='Салом! TAJIK AI кор кард!')
MyApp().run()