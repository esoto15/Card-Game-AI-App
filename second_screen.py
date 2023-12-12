from kivy.metrics import dp

import imports
import pyttsx3
from pyttsx3 import init, Engine

loteria_cards = {
    1: 'El Gallo',
    2: 'El Diablito',
    3: 'La Dama',
    4: 'El Catrín',
    5: 'El Paraguas',
    6: 'La Sirena',
    7: 'La Escalera',
    8: 'La Botella',
    9: 'El Barril',
    10: 'El Árbol',
    11: 'El Melón',
    12: 'El Valiente',
    13: 'El Gorrito',
    14: 'La Muerte',
    15: 'La Pera',
    16: 'La Bandera',
    17: 'El Bandolón',
    18: 'El Violoncello',
    19: 'La Garza',
    20: 'El Pájaro',
    21: 'La Mano',
    22: 'La Bota',
    23: 'La Luna',
    24: 'El Cotorro',
    25: 'El Borracho',
    26: 'El Negrito',
    27: 'El Corazón',
    28: 'La Sandía',
    29: 'El Tambor',
    30: 'El Camarón',
    31: 'Las Jaras',
    32: 'El Músico',
    33: 'La Araña',
    34: 'El Soldado',
    35: 'La Estrella',
    36: 'El Cazo',
    37: 'El Mundo',
    38: 'El Apache',
    39: 'El Nopal',
    40: 'El Alacrán',
    41: 'La Rosa',
    42: 'La Calavera',
    43: 'La Campana',
    44: 'El Cantarito',
    45: 'El Venado',
    46: 'El Sol',
    47: 'La Corona',
    48: 'La Chalupa',
    49: 'El Pino',
    50: 'El Pescado',
    51: 'La Palma',
    52: 'La Maceta',
    53: 'El Arpa',
    54: 'La Rana'
}


class SecondScreen(imports.Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        # ----Main Layout----
        self.layout = imports.MDBoxLayout(orientation='vertical')
        # Create the background image
        background_image = imports.Image(source='loteriaCards/background_img.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)

        # -----------------Top Navigation layout-------------------
        self.nav_layout = imports.MDBoxLayout(orientation='horizontal', size_hint=(1, None), height='48dp', spacing='10dp', _md_bg_color=(1, 1, 1, 1))
        self.nav_mnu = imports.MDAnchorLayout(anchor_x='right', anchor_y='center')
        self.nav_bck = imports.MDAnchorLayout(anchor_x='left', anchor_y='center')

        bck_button = imports.MDIconButton(icon='chevron-left', icon_size='29sp', on_release=self.switch_screen)
        mnu_button = imports.MDIconButton(icon='menu', icon_size='29sp')
        self.nav_bck.add_widget(bck_button)
        self.nav_mnu.add_widget(mnu_button)

        self.nav_layout.add_widget(self.nav_bck)
        self.nav_layout.add_widget(self.nav_mnu)
        self.layout.add_widget(self.nav_layout)

        # ---------------------Images--------------------------------
        self.image_layout = imports.MDBoxLayout(size_hint=(1, 0.098))
        self.images = []
        for i in range(1, 55):
            self.images.append("LoteriaCards/" + str(i) + ".png")
        self.current_image = 0
        self.playing = False

        self.image_widget = imports.Image(source=self.images[self.current_image])
        self.image_layout.add_widget(self.image_widget)

        self.layout.add_widget(self.image_layout)

        # ----------Function buttons(prev,play,next)----------------
        self.main_layout = imports.MDAnchorLayout(anchor_x='center', size_hint=(1, 0.02))
        self.btn_layout = imports.MDBoxLayout(orientation='horizontal', size_hint=(0.57, 0.7), radius=[20, 20, 20, 20], _md_bg_color=(1, 1, 1, 1))
        self.prev_layout1 = imports.MDAnchorLayout(anchor_x='right', anchor_y='center')
        self.play_layout2 = imports.MDAnchorLayout(anchor_x='center', anchor_y='center')
        self.next_layout3 = imports.MDAnchorLayout(anchor_x='left', anchor_y='center')

        self.prev_button = imports.MDIconButton(icon="skip-previous", icon_size='30sp', on_release=self.previous_image)
        self.play_button = imports.MDIconButton(icon="play", icon_size='30sp', on_release=self.play_pause)
        self.next_button = imports.MDIconButton(icon="skip-next", icon_size='30sp', on_release=self.next_image)

        self.prev_layout1.add_widget(self.prev_button)
        self.play_layout2.add_widget(self.play_button)
        self.next_layout3.add_widget(self.next_button)

        self.btn_layout.add_widget(self.prev_layout1)
        self.btn_layout.add_widget(self.play_layout2)
        self.btn_layout.add_widget(self.next_layout3)

        self.main_layout.add_widget(self.btn_layout)

        self.layout.add_widget(self.main_layout)
        # -----------------shuffle button-------------------------
        self.shuffle_layout = imports.MDBoxLayout(orientation='horizontal', size_hint=(1, 0.02), spacing='10dp')
        self.shuffle_anchor_lay1 = imports.MDAnchorLayout(anchor_x='right')
        self.shuffle_anchor_lay2 = imports.MDAnchorLayout(anchor_x='left')

        self.shuffle_button = imports.MDIconButton(icon='shuffle-variant')
        self.mute_button = imports.MDIconButton(icon='volume-off')

        self.shuffle_anchor_lay1.add_widget(self.shuffle_button)
        self.shuffle_anchor_lay2.add_widget(self.mute_button)

        self.shuffle_layout.add_widget(self.shuffle_anchor_lay1)
        self.shuffle_layout.add_widget(self.shuffle_anchor_lay2)

        self.layout.add_widget(self.shuffle_layout)
        # ----------------Dummy space-----------------------------
        self.temp_layout = imports.MDBoxLayout(orientation='horizontal', size_hint=(1, 0.04))
        self.layout.add_widget(self.temp_layout)
        # ---------------bottom navigation-------------------------
        self.btm_layout = imports.MDBoxLayout(orientation='horizontal', size_hint=(1, None), height='48dp', spacing='10dp', _md_bg_color=(1, 1, 1, 1), radius=[20, 20, 0, 0])
        self.layout1 = imports.MDAnchorLayout(anchor_x='right', anchor_y='bottom')
        self.layout2 = imports.MDAnchorLayout(anchor_x='center', anchor_y='bottom')
        self.layout3 = imports.MDAnchorLayout(anchor_x='left', anchor_y='bottom')

        user_btn = imports.MDIconButton(icon="home", icon_size='30sp')
        home_btn = imports.MDIconButton(icon="camera", icon_size='60sp', _theme_icon_color='Custom', md_bg_color='#fefbff')
        not_btn = imports.MDIconButton(icon="bell", icon_size='30sp')

        self.layout1.add_widget(user_btn)
        self.layout2.add_widget(home_btn)
        self.layout3.add_widget(not_btn)

        self.btm_layout.add_widget(self.layout1)
        self.btm_layout.add_widget(self.layout2)
        self.btm_layout.add_widget(self.layout3)

        self.layout.add_widget(self.btm_layout)
        # ----------completed layout------------
        self.add_widget(self.layout)

    #  Go to fi
    def switch_screen(self, *args):
        self.manager.current = 'first'

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
            self.engine.stop()  # Stop the text-to-voice

        else:
            imports.Clock.schedule_interval(self.next_image, 1)  # Change the interval as needed
            self.play_button.icon = "pause"
            self.speak_card_name()  # Speak the card name
        self.playing = not self.playing

    def update_image(self):
        self.image_widget.source = self.images[self.current_image]
        self.speak_card_name()

    def speak_card_name(self):
        card_number = self.current_image
        card_name = loteria_cards[card_number + 1]
        self.engine.say(card_name)
        self.engine.runAndWait()