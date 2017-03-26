from kivy.uix.button import Button
import math

from rendering.styles.global_styles import colors, fonts
from rendering.styles.css_manager import CSSManager


class CustomButton(Button):
    local_styles = {
        'button': {

        },
        'link': {
            'background_color': colors['opaque'],
            'font_size': fonts['sizes']['standard'],
            'color': 'inherit'
        },
        'link_nav_header': {'font_size': fonts['sizes']['h5']},
        'primary': {'color': colors['primary']}
    }

    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.css = CSSManager(self)
        self.up = True

    def on_load(self, app, window):
        pass

    def resize(self, *args):
        self.texture_update()
        self.size = self.texture_size[0] + 16, 50

    def button_pressed(self):
        print(self.color)
        if self.up:
            self.up = False
            self.color = min(1, self.color[0] + 0.2), min(1, self.color[1] + 0.2), min(1, self.color[2] + 0.2), self.color[3]
        else:
            self.up = True
            self.color = self.css.styles['color']
        print(self.color)
