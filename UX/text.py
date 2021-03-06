from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyDumbScreen(BoxLayout):  # Changed to a BoxLayout for simplicity

    def __init__(self, **kwargs):
        # Call the base class constructor :)
        # Note that this is where it will pick up on any stuff you did in the
        # .kv file (if you have one)
        super(MyDumbScreen, self).__init__(**kwargs)
        self.orientation = "vertical"

        # Here we are just creating a text input
        my_user_input = TextInput()

        # Here we add it to MyDumbScreen's widget tree.  If you skip this step,
        # you'll never see your precious widget.
        self.add_widget(my_user_input)

        # This is the label that will hold a modified version of the user's
        # input
        my_output = Label(text="initial value")
        self.add_widget(my_output)

        # Here we create a callback function
        # This callback will be called whenever the 'text' property of
        # our TextInput is modified
        def callback(instance, value):
            my_output.text = value

        # Here we "bind" the callback to the TextInput's 'text' property
        # If you skip this step, you won't see the changes ever take place
        my_user_input.bind(text=callback)


class MyApp(App):

    def build(self):
        return MyDumbScreen()


if __name__ == '__main__':
    MyApp().run()