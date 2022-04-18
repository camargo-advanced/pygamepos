import pygame
from text_button import TextButton
from utils import *


class PayButton(TextButton):
    def __init__(self, galaxy, text, text_alignment, action):
        super().__init__(
            galaxy=galaxy,
            text=text,
            text_alignment=text_alignment,
            text_size=23,
            rect=pygame.Rect(0, 0, 0, 0),
            border_width=0,
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
