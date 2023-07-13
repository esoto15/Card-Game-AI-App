import imports
from second_screen import SecondScreen
from first_screen import FirstScreen


class MyScreenManager(imports.ScreenManager):
    pass


class MyApp(imports.MDApp):
    def build(self):
        # Create an instance of the screen manager
        sm = MyScreenManager()
        # Add screens to the screen manager
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))

        return sm


if __name__ == '__main__':
    MyApp().run()
