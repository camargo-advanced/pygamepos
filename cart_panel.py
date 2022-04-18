import pygame
from cart_button import CartButton
from discount_button import DiscountButton
from panel import Panel
from pay_button import PayButton
from utils import *

SPACE = 10


class CartPanel(Panel):
    def __init__(self, galaxy, rect, border_width, border_radius):
        super().__init__(galaxy, rect, border_width, border_radius)
        self.discount_percentage = 0
        self.discount_button = None
        self.pay_button = None

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)

        # destroy discount button
        if self.discount_button:
            self.discount_button.kill()  # remove from galaxy

        # destroy pay button
        if self.pay_button:
            self.pay_button.kill()  # remove from galaxy

        if self.has_cart_items() > 0:
            # prepare discount button text
            if self.discount_percentage == 0:
                discount_button_text = 'Sem desconto'
            else:
                discount_button_text = '{discount_percentage}% de desconto R${discount_value:,.2f}'.format(
                    discount_percentage=self.discount_percentage,
                    discount_value=self.total_price()*self.discount_percentage/100)

            # create discount button and add to galaxy
            self.discount_button = DiscountButton(
                self.galaxy, discount_button_text, CENTER, self.discount_pressed_event)
            self.discount_button.rect = pygame.Rect(
                self.last_cart_item().rect)
            self.discount_button.rect.y += self.discount_button.rect.height + 3*SPACE
            self.galaxy.add_entity(self.discount_button)

            # prepare pay button text
            amount_to_pay = self.total_price() - self.total_price() * \
                self.discount_percentage/100
            pay_button_text = 'R${amount_to_pay:,.2f} PAGO!'.format(
                amount_to_pay=amount_to_pay)

            # create pay button and add to galaxy
            self.pay_button = PayButton(
                self.galaxy, pay_button_text, CENTER, None)
            self.pay_button.rect = pygame.Rect(
                self.last_cart_item().rect)
            self.pay_button.rect.bottom = self.rect.bottom - SPACE
            self.pay_button.rect.height *= 1.3
            self.galaxy.add_entity(self.pay_button)

    def render(self, surface):
        super().render(surface)

    def has_cart_items(self):
        if len(self.cart_items_list()) > 0:
            return True
        return False

    def discount_pressed_event(self, button):
        if self.discount_percentage == 15:
            self.discount_percentage = 0
        else:
            self.discount_percentage += 5

    def total_price(self):
        sum = 0.
        for entity in self.cart_items_list():
            sum += (entity.weight_variant_price +
                    entity.inclusion_variant_price)*entity.quantity
        return sum

    def cart_items_list(self):
        list = []
        for item in self.entities:
            if type(item) == CartButton:
                list.append(item)
        return list

    def last_cart_item(self):
        cart_items = self.cart_items_list()
        if len(cart_items) == 0:
            return None
        return cart_items[-1]
