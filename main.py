import imports
import pyttsx3

loteria_cards = {
    1: 'El Gallo (The Rooster)',
    2: 'El Diablito (The Little Devil)',
    3: 'La Dama (The Lady)',
    4: 'El Catrín (The Gentleman)',
    5: 'El Paraguas (The Umbrella)',
    6: 'La Sirena (The Mermaid)',
    7: 'La Escalera (The Ladder)',
    8: 'La Botella (The Bottle)',
    9: 'El Barril (The Barrel)',
    10: 'El Árbol (The Tree)',
    11: 'El Melón (The Melon)',
    12: 'El Valiente (The Brave One)',
    13: 'El Gorrito (The Little Bonnet)',
    14: 'La Muerte (The Death)',
    15: 'La Pera (The Pear)',
    16: 'La Bandera (The Flag)',
    17: 'El Bandolón (The Mandolin)',
    18: 'El Violoncello (The Cello)',
    19: 'La Garza (The Heron)',
    20: 'El Pájaro (The Bird)',
    21: 'La Mano (The Hand)',
    22: 'La Bota (The Boot)',
    23: 'La Luna (The Moon)',
    24: 'El Cotorro (The Parrot)',
    25: 'El Borracho (The Drunk)',
    26: 'El Negrito (The Little Black One)',
    27: 'El Corazón (The Heart)',
    28: 'La Sandía (The Watermelon)',
    29: 'El Tambor (The Drum)',
    30: 'El Camarón (The Shrimp)',
    31: 'Las Jaras (The Arrows)',
    32: 'El Músico (The Musician)',
    33: 'La Araña (The Spider)',
    34: 'El Soldado (The Soldier)',
    35: 'La Estrella (The Star)',
    36: 'El Cazo (The Saucepan)',
    37: 'El Mundo (The World)',
    38: 'El Apache (The Apache)',
    39: 'El Nopal (The Cactus)',
    40: 'El Alacrán (The Scorpion)',
    41: 'La Rosa (The Rose)',
    42: 'La Calavera (The Skull)',
    43: 'La Campana (The Bell)',
    44: 'El Cantarito (The Little Jug)',
    45: 'El Venado (The Deer)',
    46: 'El Sol (The Sun)',
    47: 'La Corona (The Crown)',
    48: 'La Chalupa (The Canoe)',
    49: 'El Pino (The Pine Tree)',
    50: 'El Pescado (The Fish)',
    51: 'La Palma (The Palm Tree)',
    52: 'La Maceta (The Flowerpot)',
    53: 'El Arpa (The Harp)',
    54: 'La Rana (The Frog)'
}


class FirstScreen(imports.Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        # ----Main Layout----
        self.layout = imports.MDBoxLayout(orientation='vertical', _md_bg_color=(0, 1, 1, 1))

        # Top Navigation layout
        self.nav_layout = imports.MDBoxLayout(orientation='horizontal', size_hint=(1, None), height='48dp', spacing='10dp', _md_bg_color=(1, 1, 1, 1))
        # Nav button-anchor-layouts
        self.nav_mnu = imports.MDAnchorLayout(anchor_x='right', anchor_y='center')
        self.nav_bck = imports.MDAnchorLayout(anchor_x='left', anchor_y='center')
        # Nav button
        bck_button = imports.MDIconButton(icon='chevron-left', icon_size='27sp', on_release=self.switch_screen)
        mnu_button = imports.MDIconButton(icon='menu', icon_size='27sp')
        self.nav_bck.add_widget(bck_button)
        self.nav_mnu.add_widget(mnu_button)

        self.nav_layout.add_widget(self.nav_bck)
        self.nav_layout.add_widget(self.nav_mnu)
        #  add to main
        self.layout.add_widget(self.nav_layout)

        # Images
        self.images = []
        for i in range(1, 55):
            self.images.append("LoteriaCards/" + str(i) + ".png")
        self.current_image = 0
        self.playing = False

        self.image_widget = imports.Image(source=self.images[self.current_image])
        self.image_widget.size_hint = (1, 1)
        self.layout.add_widget(self.image_widget)
        # Function buttons(prev,play,next)
        self.btn_layout = imports.MDGridLayout(cols=3, pos_hint={"x": 0.28})
        self.prev_button = imports.MDIconButton(icon="skip-previous", icon_size='35sp', on_release=self.previous_image)
        self.play_button = imports.MDIconButton(icon="play", icon_size='35sp', on_release=self.play_pause)
        self.next_button = imports.MDIconButton(icon="skip-next", icon_size='35sp', on_release=self.next_image)
        self.btn_layout.add_widget(self.prev_button)
        self.btn_layout.add_widget(self.play_button)
        self.btn_layout.add_widget(self.next_button)
        self.layout.add_widget(self.btn_layout)

        # ---------------bottom navigation--------------
        self.btn_layout = imports.MDGridLayout(cols=3)
        self.home_btn = imports.MDIconButton(icon="skip-previous", icon_size='35sp', on_release=self.previous_image)
        self.home_btn = imports.MDIconButton(icon="skip-previous", icon_size='35sp', on_release=self.previous_image)
        self.home_btn = imports.MDIconButton(icon="skip-previous", icon_size='35sp', on_release=self.previous_image)

        self.add_widget(self.layout)

    def switch_screen(self, *args):
        self.manager.current = 'second'

    def previous_image(self, *args):
        if self.current_image > 0:
            self.current_image -= 1
            self.update_image()

    def next_image(self, *args):
        if self.current_image < len(self.images) - 1:
            self.current_image += 1
            self.update_image()

    def play_pause(self, *args):
        if self.playing:
            imports.Clock.unschedule(self.next_image)
            self.play_button.icon = "play"
        else:
            imports.Clock.schedule_interval(self.next_image, 1)  # Change the interval as needed
            self.play_button.icon = "pause"
        self.playing = not self.playing

    def update_image(self):
        self.image_widget.source = self.images[self.current_image]
        self.speak_card_name()

    def speak_card_name(self):
        card_number = self.current_image
        card_name = loteria_cards[card_number]
        self.engine.say(card_name)
        self.engine.runAndWait()


class SecondScreen(imports.Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = imports.MDBoxLayout(orientation='vertical')
        label = imports.MDLabel(text='Second Screen')
        button = imports.MDFlatButton(text='Go to First Screen', on_release=self.switch_screen)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_screen(self, *args):
        self.manager.current = 'first'


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
