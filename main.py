from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock

class RandomListChooser(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        Window.clearcolor = (0.8, 0.8, 0.8, 1)
        self.label1=Label(text="", color=(0, 0, 0, 1))
        self.window.add_widget(self.label1)
        self.goto=Button(text="Generate Random place!")
        self.window.add_widget(self.goto)
        self.goto.bind(on_press=self.callback)
        self.count=0
        self.text=open('rig.txt', 'r+').readlines()
        return self.window

    def callback(self, instance):
        self.label1.text=self.text[self.count]
        self.count += 1

if __name__ == "__main__":
    RandomListChooser().run()