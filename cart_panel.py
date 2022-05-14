import pygame
from cart_button import CartButton
from discount_button import DiscountButton
from label import Label
from panel import Panel
from pay_button import PayButton
from payment_method import PaymentMethod
from datetime import datetime
from utils import *

SPACE = 7


class CartPanel(Panel):
    def __init__(self, galaxy, rect, border_width, border_radius):
        super().__init__(galaxy, rect, border_width, border_radius)
        self.discount_button = None
        self.payment_methods = [
                'Cartão de débito',
                'Cartão de crédito',
                'Pix',
                'Dinheiro'
            ]
        self.payment_method_button = None
        self.pay_button = None
        self.reset()
        self.dirty = True

    def update(self, time_passed, event_list):
        super().update(time_passed, event_list)
        if self.dirty == True:
            self.dirty = False
            self.build()

    def render(self, surface):
        super().render(surface)

    def reset(self):
        self.discount_percentage = 0
        self.payment_method_index = 0
        for item in self.entities:
            item.kill() # remove from galaxy
        self.entities.clear()

        # add cart panel label
        cart_label = Label(self.galaxy,
                               text='Carrinho de compras:',
                               text_alignment=LEFT,
                               rect=pygame.Rect(0, 0, 250, 25))
        self.add_entity(cart_label)
        self.galaxy.add_entity(cart_label)

    def build(self):
        # destroy payment method, discount and pay buttons
        if self.payment_method_button: self.payment_method_button.kill()
        if self.discount_button: self.discount_button.kill()  
        if self.pay_button: self.pay_button.kill()  

        if self.has_cart_items() > 0:
            # prepare payment method button text
            payment_method_button_text = self.payment_methods[self.payment_method_index]

            # create payment method button and add to galaxy
            self.payment_method_button = PaymentMethod(
                self.galaxy, payment_method_button_text, CENTER, self.payment_method_pressed_event)
            self.payment_method_button.rect = pygame.Rect(
                self.last_cart_item().rect)
            self.payment_method_button.rect.y += self.payment_method_button.rect.height + 3*SPACE
            self.payment_method_button.rect.height /= 1.4
            self.galaxy.add_entity(self.payment_method_button)

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
            self.discount_button.rect = pygame.Rect(self.payment_method_button.rect)
            self.discount_button.rect.y += self.discount_button.rect.height + SPACE
            self.galaxy.add_entity(self.discount_button)

            # prepare pay button text
            amount_to_pay = self.total_price() - self.total_price() * \
                self.discount_percentage/100
            pay_button_text = 'R${amount_to_pay:,.2f} PAGO!'.format(
                amount_to_pay=amount_to_pay)

            # create pay button and add to galaxy
            self.pay_button = PayButton(
                self.galaxy, pay_button_text, CENTER, self.pay_pressed_event)
            self.pay_button.rect = pygame.Rect(
                self.last_cart_item().rect)
            self.pay_button.rect.bottom = self.rect.bottom - 2*SPACE
            self.galaxy.add_entity(self.pay_button)

    def rebuild(self):
        self.dirty = True

    def has_cart_items(self):
        if len(self.cart_items_list()) > 0:
            return True
        return False

    def payment_method_pressed_event(self, button):
        self.dirty = True
        if self.payment_method_index == 3:
            self.payment_method_index = 0
        else:
            self.payment_method_index += 1

    def discount_pressed_event(self, button):
        self.dirty = True
        if self.discount_percentage == 15:
            self.discount_percentage = 0
        else:
            self.discount_percentage += 5

    def pay_pressed_event(self, button):
        self.cart_number = datetime.now().strftime("%d%m%y-%H%M%S")
        row = ''
        for entity in self.cart_items_list():
            row += self.cart_number + ', '
            row += str(entity.quantity) + ', '
            row += entity.text1 + ' ' + entity.text2 + '\n'
            
        row += self.cart_number + ', '
        row += self.payment_method_button.text + ', '
        row += self.discount_button.text + ', '
        amount_to_pay = self.total_price() - self.total_price() * \
                self.discount_percentage/100
        amount_to_pay_text = '{amount_to_pay:,.2f}'.format(
                amount_to_pay=amount_to_pay)
        row += amount_to_pay_text + '\n'
        filename = '../' + datetime.now().strftime("%d%m%y") + '.csv'
        with open(filename, 'a') as f:
            f.write(row)
        self.reset()
        self.build() 

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
