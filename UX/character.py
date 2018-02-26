import kivy
import plyer

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
from kivy.properties import StringProperty
from plyer import gps

Builder.load_string("""

<CustLabel@Label>:
    color: 0, 0, 0, 1

<LoginScreen>:
    canvas:
        Color:
            rgb: [.5,.5,.95]
        Rectangle:
            pos:self.pos
            size:self.size
    RelativeLayout:
        Button:
            text: 'Character Page'
            pos: (root.width*0.8, root.y)
            size_hint: .2,.1
            on_press: 
                root.manager.current = 'main'
                root.manager.transition.direction = 'left'
        Label:
            text: "Welcome to your Dreamscape:"
            pos: (root.width*.25, root.height*.35)
            size_hint: .5,.8
        Label:
            text: "Drogens and Dungoons"
            pos: (root.width*.25, root.height*.25)
            size_hint: .5,.8
    GridLayout:
        orientation: "horizontal"
        rows:1
        cols:3
        size_hint: .3,.1
        pos: (root.width*.35,root.height*.5)
        Spinner:
            text: 'Name'
            values: ["Majones", "Cryan Blark", "Sexlando", "Bobert"]
            id: spinner_id
            on_text: root.spinner_clicked(spinner_id.text)
        Spinner:
            text: 'Class'
            values: ["cleric", "wizard", "rogue", "fighter"]
            id: spinner_id
            on_text: root.spinner_clicked(spinner_id.text)
        Spinner:
            text: 'Race'
            values: ["Dwarf", "Elf", "Halfing", "Human"]
            id: spinner_id
            on_text: root.spinner_clicked(spinner_id.text)
    GridLayout:
        RelativeLayout:
            orientation: "horizontal"
            pos: root.width*.1, root.height*.3
            size_hint: .4, 0.2
            CustLabel:
                text: str(slider_id.value)
            Slider:
                id: slider_id
                min: 0
                max: 30
                value: 0
                step: 1


<MainScreen>:
    canvas:
        Color:
            rgb: [.5,.5,.95]
        Rectangle:
            pos:self.pos
            size:self.size
    RelativeLayout:
        Image:
            source: "../Images/Characters/Dwarf cleric.png"
            pos: (root.width*.4, root.height*.45)
            size_hint: .2, .6
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
            pos: (root.width*.4, root.height*.36)
            size_hint: .2,.1
            # When clicked the popup opens
            Button:
                text: "Stats"
                on_press: root.open_popup()
    RelativeLayout:
        Label:
            text: "HP: 10"
            pos: (root.width*(.4-.2), root.height*.44)
            size_hint: .2,.1
        Label:
            text: "AC: 10"
            pos: (root.width*.4, root.height*.44)
            size_hint: .2,.1
        Label:
            text: "SP: 10"
            pos: (root.width*(.4+0.2), root.height*.44)
            size_hint: .2,.1
        Label:
            text: "Race: Human   /  Name: Marissa Jones   /   Level: 10   /   Class: Fighter"
            pos: (root.width*.1, root.height*.5)
            size_hint: .8,.05
        Label:
            text: "This is going to be a description of the fighter"
            pos: (root.width*.1, root.height*.25)
            size_hint: .8,.05

<SecondScreen>:
    canvas:
        Color:
            rgb: [.5,.5,.95]
        Rectangle:
            pos:self.pos
            size:self.size
    RelativeLayout:
        Button:
            text: 'Character Stats'
            pos: (root.x, root.y)
            size_hint: .2,.1
            on_press: 
                root.manager.current = 'main'
                root.manager.transition.direction = 'right'
        Spinner:
            text: 'Weapons'
            pos: (root.width*.25,root.height*.8)
            size_hint: 0.5,.1
            values: ["Big Ass Rifle", "GUNZZZZ", "Gun That Shoots Other Guns"]
            id: spinner_id
            on_text: root.spinner_clicked(spinner_id.text)
        Spinner:
            text: 'Armor'
            pos: (root.width*.25,root.height*.4)
            size_hint: 0.5,.1
            values: ["Big Ass Shield", "Nudity", "CS Virgin"]
            id: spinner_id
            on_text: root.spinner_clicked(spinner_id.text)

<ThirdScreen>:
    canvas:
        Color:
            rgb: [.5,.5,.95]
        Rectangle:
            pos:self.pos
            size:self.size
    RelativeLayout:
        Button:
            text: 'Character Stats'
            pos: (root.width*0.8, root.y)
            size_hint: .2,.1
            on_press: 
                root.manager.current = 'main'
                root.manager.transition.direction = 'left'
        Painter:
            pos: (root.width*0.8, root.height/2)
    GridLayout:
        orientation: "horizontal"
        rows:4
        cols:1
        size_hint: .5,.4
        Button:
            text: "Action"
            on_press: root.open_popup()
        Button:
            text: "Bonus"
            on_press: root.open_popup()
        Button:
            text: "Move"
            on_press: root.open_popup()
        Button:
            text: "Inventory"
            on_press: root.open_popup()

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

<ActionPopup>:
    title: "Action"
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

class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]

class CustomPopup(Popup):
    pass

class ActionPopup(Popup):
    pass

class BonusPopup(Popup):
    pass

class MovePopup(Popup):
    pass

class InventoryPopup(Popup):
    pass

class Painter(Widget):
    
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]

class LoginScreen(Screen):
    def spinner_clicked(self, value):
        print("Spinner Value " + value)

class MainScreen(Screen):
    #toggle drop down menu
    def spinner_clicked(self, value):
        print("Spinner Value " + value)
        # Opens Popup when called
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

class SecondScreen(Screen):
    # For Spinner
    def spinner_clicked(self, value):
        print("Spinner Value " + value)

class ThirdScreen(Screen):
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()    

sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SecondScreen(name='second'))
sm.add_widget(ThirdScreen(name='third'))

class TestApp(App):
    gps_location = StringProperty()
    gps_status = StringProperty("Null")

    def build(self):
        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = "No GPS support"
        return sm

    def on_location(self, **kwargs):
        self.gps_location = '\n'.join(['{}={}'.format(k, v) for k, v in kwargs.items()])

    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)
		
test_app = TestApp()
test_app.run()