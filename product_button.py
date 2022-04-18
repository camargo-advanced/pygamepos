import pygame
from text_button import TextButton
from utils import *

BUTTON_WIDTH = 120
BUTTON_HEIGHT = BUTTON_WIDTH * 0.35


class ProductButton(TextButton):
    def __init__(self, galaxy, text, action):
        super().__init__(
            galaxy=galaxy,
            text=text,
            text_alignment=CENTER,
            text_size=19,
            rect=pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT),
            border_width=1,
            border_radius=3,
            double_border=False,
            action=action)

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)
        self.process_events(event_list)

    def process_events(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > self.rect.x and x < self.rect.x+self.rect.width and \
                        y > self.rect.y and y < self.rect.y+self.rect.height:
                    self.action(self)
