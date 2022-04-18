import pygame
import os
from entity import Entity
from utils import *


class TextButton2(Entity):
    def __init__(self, galaxy, text1, text2, text_size, rect, border_width, border_radius, action):
        super().__init__(galaxy, id(self))
        self.text1 = text1
        self.text2 = text2
        self.rect = rect
        self.border_width = border_width
        self.border_radius = border_radius
        self.action = action
        self.font = pygame.font.Font(os.path.join(
            'res', 'fonts', 'arial-rounded-bold.ttf'), text_size)

    def render(self, surface):
        super().render(surface)
        if not self.visible: return 

        # render button
        pygame.draw.rect(
            surface=surface,
            color=GREEN,
            rect=self.rect,
            width=self.border_width,
            border_radius=self.border_radius)

        # render line 1 of text
        self.font_surface = self.font.render(self.text1, True, GREEN, BLACK)
        self.font_surface_rect = self.font_surface.get_rect()
        self.font_surface_rect.centerx = self.rect.centerx
        self.font_surface_rect.centery = self.rect.top + 2*self.rect.height/7
        surface.blit(self.font_surface, self.font_surface_rect)

        # render line 2 of text
        self.font_surface = self.font.render(self.text2, True, GREEN, BLACK)
        self.font_surface_rect = self.font_surface.get_rect()
        self.font_surface_rect.centerx = self.rect.centerx
        self.font_surface_rect.centery = self.rect.bottom - 2*self.rect.height/7
        surface.blit(self.font_surface, self.font_surface_rect)
