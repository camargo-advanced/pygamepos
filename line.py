import pygame
from entity import Entity
from utils import *


class Line(Entity):
    def __init__(self, galaxy, start_pos, end_pos, width):
        super().__init__(galaxy, id(self))
        self.start_pos, self.end_pos, self.width = start_pos, end_pos, width

    def render(self, surface):
        super().render(surface)
        if not self.visible: return 
        pygame.draw.line(surface, GREEN, self.start_pos,
                         self.end_pos, self.width)
