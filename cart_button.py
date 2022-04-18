import pygame
import os
import pygame.gfxdraw
from text_button2 import TextButton2
from utils import *

BUTTON_WIDTH = 250
BUTTON_HEIGHT = BUTTON_WIDTH * 0.19


class CartButton(TextButton2):
    def __init__(self, galaxy, category_name, product_name, left_action, right_action):
        super().__init__(
            galaxy=galaxy,
            text1='',
            text2='',
            text_size=17,
            rect=pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT),
            border_width=1,
            border_radius=3,
            action=None)
        self.category_name = category_name
        self.product_name = product_name
        self.left_action = left_action
        self.right_action = right_action
        self.quantity = 1
        self.weight_variant_value = ''
        self.weight_variant_price = 0.
        self.inclusion_variant_value = ''
        self.inclusion_variant_price = 0.
        self.qtd_font = pygame.font.Font(os.path.join(
            'res', 'fonts', 'arial-rounded-bold.ttf'), 19)

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)
        self.process_events(event_list)

    def process_events(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > self.rect.x and x < self.rect.x+self.rect.width/2 and \
                        y > self.rect.y and y < self.rect.y+self.rect.height:
                    self.left_action(self)
                if x > self.rect.x+self.rect.width/2 and x < self.rect.x+self.rect.width and \
                        y > self.rect.y and y < self.rect.y+self.rect.height:
                    self.right_action(self)
        self.text1 = '{category_name} {product}'.format(
            category_name=self.category_name,
            product=self.product_name)
        self.text2 = '{weight} {inclusion} R${price:,.2f}'.format(
            weight=self.weight_variant_value,
            inclusion=self.inclusion_variant_value,
            price=(self.weight_variant_price+self.inclusion_variant_price)*self.quantity)

    def render(self, surface):
        super().render(surface)
        if not self.visible:
            return

        # draw an anti-alised circle - border + fills it
        pygame.gfxdraw.aacircle(
            surface, int(self.rect.x+self.rect.width),
            int(self.rect.y+self.rect.height/2), int(self.rect.height*0.7/2), GREEN)
        pygame.gfxdraw.filled_circle(
            surface, int(self.rect.x+self.rect.width),
            int(self.rect.y+self.rect.height/2), int(self.rect.height*0.7/2), GREEN)

        # render quantity
        self.qtd_font_surface = self.qtd_font.render(
            str(self.quantity), True, BLACK, GREEN)
        self.qtd_font_surface_rect = self.qtd_font_surface.get_rect()
        self.qtd_font_surface_rect.center = [int(self.rect.x+self.rect.width),
                                             int(self.rect.y+self.rect.height/2)]
        surface.blit(self.qtd_font_surface, self.qtd_font_surface_rect)


    def product_category_prefix(self):
        if self.category_name == 'Ovo':
            prefix = 'O'
        elif self.category_name == 'Barra':
            prefix = 'B'
        elif self.category_name == 'Bombom':
            prefix = 'BB'
        return prefix 

    def increment(self):
        self.quantity += 1

    def decrement(self):
        self.quantity -= 1

    def update_weight_variant(self, variant_value, variant_price):
        self.weight_variant_value = variant_value
        self.weight_variant_price = variant_price

    def update_inclusion_variant(self, variant_value, variant_price):
        self.inclusion_variant_value = variant_value
        self.inclusion_variant_price = variant_price
