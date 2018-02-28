import kivy
import plyer
from kivy.graphics import BorderImage
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

Builder.load_file('character.kv')
Character_Name = "No Name"
Class_Name = ""


class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]

class StatsPopup(Popup):
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
    def save_name(self):
        global Character_Name
        Character_Name = self.ids.full_name.text
    def save_class(self, value):
        global Class_Name
        Class_Name = self.ids.class_name.text

class MainScreen(Screen):
    #toggle drop down menu
    def store_description(self):
        global Character_Name
        global Class_Name
        self.ids.description.text = Character_Name + " / " + Class_Name
        self.ids.image.source = "Images/Characters/" + Class_Name + ".png"
        # Opens Popup when called
    def open_popup(self):
        the_popup = StatsPopup()
        the_popup.open()

class SecondScreen(Screen):
    # For Spinner
    def spinner_clicked(self, value):
        print("Spinner Value " + value)

class ThirdScreen(Screen):
    def open_action_popup(self):
        the_popup = ActionPopup()
        the_popup.open()
    def open_bonus_popup(self):
        the_popup = BonusPopup()
        the_popup.open()
    def open_move_popup(self):
        the_popup = MovePopup()
        the_popup.open()
    def open_inventory_popup(self):
        the_popup = InventoryPopup()
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