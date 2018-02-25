import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics import Line

Builder.load_string("""
<MainScreen>:
    RelativeLayout:
        Image:
            source: "smiley.png"
            pos: (root.width*.375, root.height*.5)
            size_hint: .25,.5
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
        Spinner:
            text: "First"
            pos: (root.width/4, root.height/4)
            size_hint: .1,.1
            values: ["First", "Second", "Third"]
            id: spinner_id
            on_text: root.spinner_clicked(spinner_id.text)

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
""")

class Painter(Widget):
    
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]

class MainScreen(Screen):
    def spinner_clicked(self, value):
        print("Spinner Value " + value)

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
