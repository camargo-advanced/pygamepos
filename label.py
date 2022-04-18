import pygame
from text_button import TextButton
from utils import *


class Label(TextButton):
    def __init__(self, galaxy, text, text_alignment, rect):
        super().__init__(
            galaxy=galaxy,
            text=text,
            text_size=17,
            text_alignment=text_alignment,
            rect=rect,
            border_width=-1,
            border_radius=3,
            double_border=False,
            action=None)
