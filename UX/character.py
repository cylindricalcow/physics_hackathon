import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics import Line
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

Builder.load_string("""
<MainScreen>:
    canvas:
        Color:
            rgb: [.5,.5,.95]
        Rectangle:
            pos:self.pos
            size:self.size
    RelativeLayout:
        Image:
            source: "../Images/Characters/Human fighter.png"
            pos: (root.width*.375, root.height*.2)
            size_hint: .25,.7
        Button:
            text: 'Inventory'
            pos: (root.width*0.8, root.y)
            size_hint: .2,.1
            on_press: 
                root.manager.current = 'second'
                root.manager.transition.direction = 'left'
        Button:
            text: 'Map'
            pos: (root.x, root.y)
            size_hint: .2,.1
            on_press: 
                root.manager.current = 'third'
                root.manager.transition.direction = 'right'
        RelativeLayout:
            orientation: "horizontal"
            pos: (root.width*.4, root.height*.15)
            size_hint: .2,.1
            # When clicked the popup opens
            Button:
                text: "Stats"
                on_press: root.open_popup()
    GridLayout:
        Label:
            text: "Health Points: 10"
            size_hint: .15,.05
            pos: (root.width*0.85/3, root.height/4)
        Label:
            text: "Armor Class: 10"
            size_hint: .15,.05
            pos: (root.width*0.85/2, root.height/4)
        Label:
            text: "Speed: 10"
            size_hint: .15,.05
            pos: (root.width*.85, root.height/4)


<SecondScreen>:
    RelativeLayout:
    	Button:
            text: 'Character Stats'
            pos: (root.x, root.y)
            size_hint: .2,.1
            on_press: 
                root.manager.current = 'main'
                root.manager.transition.direction = 'right'

<ThirdScreen>:
    RelativeLayout:
        Button:
            text: 'Character Stats'
            pos: (root.width*0.8, root.y)
            size_hint: .2,.1
            on_press: 
                root.manager.current = 'main'
                root.manager.transition.direction = 'left'

<CustomPopup>:
    title: "Stats"
    size_hint: .5, .5
    auto_dismiss: False
    GridLayout:
        cols: 3
        rows: 3
        pos: root.x, root.height
        Label:
            text: "STR: 10"
        Label:
            text: "DEX: 10"
        Label:
            text: "CON: 10"
        Label:
            text: "INT: 10"
        Label:
            text: "WIS: 10"
        Label:
            text: "CHA: 10"
        Label:
            size_hint:.2,.2
        Button:
            size_hint:.2,.2
            text: "Close"
            on_press: root.dismiss()
        Label:
            size_hint:.2,.2
""")

class CustomPopup(Popup):
    pass
 

class Painter(Widget):
    
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]

class MainScreen(Screen):
    #toggle drop down menu
    def spinner_clicked(self, value):
        print("Spinner Value " + value)
        # Opens Popup when called
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

class SecondScreen(Screen):
	pass

class ThirdScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SecondScreen(name='second'))
sm.add_widget(ThirdScreen(name='third'))

class TestApp(App):
	def build(self):
		return sm
		
test_app = TestApp()
test_app.run()
