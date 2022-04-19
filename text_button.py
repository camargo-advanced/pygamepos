import pygame
import os
from entity import Entity
from utils import *


class TextButton(Entity):
    def __init__(self, galaxy, text, text_size, text_alignment, rect, border_width, border_radius, double_border, action):
        super().__init__(galaxy, id(self))
        self.text = text
        self.text_alignment = text_alignment
        self.rect = rect
        self.border_width = border_width
        self.border_radius = border_radius
        self.double_border = double_border
        self.action = action
        self.font = pygame.font.Font(os.path.join(
            'res', 'fonts', 'arial-rounded-bold.ttf'), text_size)

    def render(self, surface):
        super().render(surface)
        if not self.visible:
            return

        # render button
        pygame.draw.rect(
            surface=surface,
            color=GREEN,
            rect=self.rect,
            width=self.border_width,
            border_radius=self.border_radius)

        if self.double_border:
            rect2 = pygame.Rect(self.rect)
            rect2.x += 4
            rect2.y += 4
            rect2.width -= 8
            rect2.height -= 8
            pygame.draw.rect(
                surface=surface,
                color=GREEN,
                rect=rect2,
                width=self.border_width,
                border_radius=self.border_radius)

        # render button text
        if self.border_width == 0: # filled button
            self.font_surface = self.font.render(self.text, True, BLACK, GREEN)
        else:
            self.font_surface = self.font.render(self.text, True, GREEN, BLACK)
        self.font_surface_rect = self.font_surface.get_rect()
        if self.text_alignment == LEFT:
            self.font_surface_rect.left = self.rect.left
            self.font_surface_rect.centery = self.rect.centery
        else:
            self.font_surface_rect.center = self.rect.center
        surface.blit(self.font_surface, self.font_surface_rect)
