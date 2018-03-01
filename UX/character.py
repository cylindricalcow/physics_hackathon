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
import random
import numpy as np

Character_Name = "Mr. Smiley"
Class_Name = "Circular Ellipse"
Random_Stats = np.zeros(6, int)
Modifiers = np.zeros(6, int)
Random_Attributes = np.zeros(3,int)
Builder.load_file('character.kv')


class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]

class StatsPopup(Popup):
    def store_stats_and_mods(self):
        global Random_Stats
        self.ids.stats0.text, self.ids.stats1.text, self.ids.stats2.text, self.ids.stats3.text, self.ids.stats4.text, self.ids.stats5.text  = "STR: " + str(Random_Stats[0]) + "\n" + "MOD: " + str(Modifiers[0]), "DEX: " + str(Random_Stats[1])+ "\n" + "MOD: " + str(Modifiers[1]), "CON: " + str(Random_Stats[2])+ "\n" + "MOD: " + str(Modifiers[2]), "INT: " + str(Random_Stats[3])+ "\n" + "MOD: " + str(Modifiers[3]), "WIS: " + str(Random_Stats[4])+ "\n" + "MOD: " + str(Modifiers[4]), "CHA: " + str(Random_Stats[5])+ "\n" + "MOD: " + str(Modifiers[5])


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
    def save_name(self):
        global Character_Name
        Character_Name = self.ids.full_name.text
    def save_class(self, value):
        global Class_Name
        Class_Name = self.ids.class_name.text
    def save_stats(self, index):
        global Random_Stats
        status = {0:self.ids.str_name.text,
                  1:self.ids.dex_name.text,
                  2:self.ids.con_name.text,
                  3:self.ids.wis_name.text,
                  4:self.ids.int_name.text,
                  5:self.ids.cha_name.text}[index]
        mod = {0:self.ids.str_mod_name.text,
                1:self.ids.dex_mod_name.text,
                2:self.ids.con_mod_name.text,
                3:self.ids.wis_mod_name.text,
                4:self.ids.int_mod_name.text,
                5:self.ids.cha_mod_name.text}[index]
        if ((status == '') or (mod == '')): #or (type(status[index]) is not int)
           return
        Random_Stats[index] = int(status)
        Modifiers[index] = int(mod)
    def save_attributes(self, index):
        global Random_Attributes
        attributes = {0:self.ids.hp_name.text,
                      1:self.ids.ac_name.text,
                      2:self.ids.sp_name.text}[index]
        if ((attributes == '')):
            return
        Random_Attributes[index] = int(attributes)

class MainScreen(Screen):
    #toggle drop down menu
    def store_description(self):
        global Character_Name
        global Class_Name
        self.ids.description.text = "Name: " + Character_Name + " / Class: " + Class_Name
        self.ids.character_image.source = "Images/Characters/" + Class_Name + ".png"
    #Opens Popup when called
    def open_popup(self):
        the_popup = StatsPopup()
        the_popup.store_stats_and_mods()
        the_popup.open()
    def store_attributes(self):
        global Random_Attributes
        self.ids.attributes0.text, self.ids.attributes1.text, self.ids.attributes2.text = "HP: " + str(Random_Attributes[0]), "AC: " + str(Random_Attributes[1]), "SP: " + str(Random_Attributes[2])


class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    def open_popup(self, index):
        the_popup = {0: ActionPopup(), 1: BonusPopup(), 2:MovePopup(), 3: InventoryPopup()}[index]
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