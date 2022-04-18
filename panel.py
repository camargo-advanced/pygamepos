import pygame
from discount_button import DiscountButton
from entity import Entity
from utils import *

SPACE = 10


class Panel(Entity):
    def __init__(self, galaxy, rect, border_width, border_radius):
        super().__init__(galaxy, id(self))
        self.rect = rect
        self.border_width = border_width
        self.border_radius = border_radius
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def clear(self):
        self.entities.clear()

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

        # Update entities position
        width_available = self.rect.width
        x = self.rect.left
        y = self.rect.top
        last_height = 0
        for entity in self.entities:
            if width_available < SPACE + entity.rect.width:
                width_available = self.rect.width
                x = self.rect.left
                y += last_height+SPACE
                last_height = 0
            entity.rect.x = x
            entity.rect.y = y
            x += SPACE + entity.rect.width
            width_available -= SPACE + entity.rect.width
            last_height = entity.rect.height
            entity.active = True

    def render(self, surface):
        super().render(surface)
        if not self.visible: return 

        self.element = pygame.draw.rect(
            surface=surface,
            color=GREEN,
            rect=pygame.Rect(self.rect.left, self.rect.top,
                             self.rect.width, self.rect.height),
            width=self.border_width,
            border_radius=self.border_radius)
