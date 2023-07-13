import imports


class FirstScreen(imports.Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)

        # Create the background image
        background = imports.Image(source='loteriaCards/background_img.jpg', allow_stretch=True, keep_ratio=False)

        # Create the main layout
        layout = imports.MDBoxLayout(orientation='vertical')
        label = imports.MDLabel(text='First Screen')
        button = imports.MDFlatButton(text='Go to Second Screen', on_release=self.switch_screen)

        layout.add_widget(label)
        layout.add_widget(button)

        # Add the background and layout to the screen
        self.add_widget(background)
        self.add_widget(layout)

    # Go to the second screen
    def switch_screen(self, *args):
        self.manager.current = 'second'