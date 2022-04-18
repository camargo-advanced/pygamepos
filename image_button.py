import pygame
import os
from entity import Entity


class ImageButton(Entity):
    def __init__(self, galaxy, text, image_name, rect, action):
        super().__init__(galaxy, id(self))
        self.text = text
        self.rect = rect
        self.action = action
        self.image_surface = pygame.image.load(os.path.join(
            'res', 'images', image_name)).convert()
        self.image_surface = pygame.transform.smoothscale(
            self.image_surface, (self.rect.width, self.rect.height))

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)
        self.process_events(event_list)

    def process_events(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > self.rect.left and x < self.rect.left+self.rect.width and \
                        y > self.rect.top and y < self.rect.top+self.rect.height:
                    self.action(self)

    def render(self, surface):
        super().render(surface)
        if not self.visible: return 
        surface.blit(self.image_surface, (self.rect.left, self.rect.top))
