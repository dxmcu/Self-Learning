import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.button import Button
 
class TestApp(App):
    def build(self):
        return Button(text="Hello,kivy")
TestApp().run()