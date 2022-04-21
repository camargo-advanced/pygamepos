import pygame
from cart_button import CartButton
from cart_panel import CartPanel
from label import Label
from product_button import ProductButton
from image_button import ImageButton
from panel import Panel
from line import Line
from inventory import Inventory
from datetime import datetime
from utils import *


class Sales():
    def __init__(self, galaxy):
        self.galaxy = galaxy
        self.selected_category_name = 'Barra'
        self.selected_product_name = None
        self.inventory = Inventory()
        self.build()

    def build(self):
        panel_window = Panel(self.galaxy,
                             rect=pygame.Rect(
                                 self.galaxy.rect.left+3, self.galaxy.rect.top+3,
                                 self.galaxy.rect.width-6, self.galaxy.rect.height-6),
                             border_width=2,
                             border_radius=9)
        self.galaxy.add_entity(panel_window)

        # add category options
        self.galaxy.add_entity(ImageButton(self.galaxy,
                                           text='Barra',
                                           image_name='bar.png',
                                           rect=pygame.Rect(10, 30, 60, 60),
                                           action=self.category_pressed_event))

        self.galaxy.add_entity(ImageButton(self.galaxy,
                                           text='Avelã',
                                           image_name='jar.png',
                                           rect=pygame.Rect(10, 100, 60, 60),
                                           action=self.category_pressed_event))

        self.galaxy.add_entity(ImageButton(self.galaxy,
                                           text='Bombom',
                                           image_name='candy.png',
                                           rect=pygame.Rect(10, 170, 60, 60),
                                           action=self.category_pressed_event))

        self.galaxy.add_entity(ImageButton(self.galaxy,
                                           text='Amendoim',
                                           image_name='jar.png',
                                           rect=pygame.Rect(10, 240, 60, 60),
                                           action=self.category_pressed_event))

        self.galaxy.add_entity(ImageButton(self.galaxy,
                                           text='Ovo',
                                           image_name='egg.png',
                                           rect=pygame.Rect(10, 310, 60, 60),
                                           action=self.category_pressed_event))

        # products panel
        self.products_panel = Panel(self.galaxy,
                                    rect=pygame.Rect(100, 15, 390, 460),
                                    border_width=-1,
                                    border_radius=3)
        self.galaxy.add_entity(self.products_panel)

        # first line separator
        self.galaxy.add_entity(Line(self.galaxy,
                                    start_pos=[80, 20],
                                    end_pos=[80, 460],
                                    width=2))

        self.build_products_panel()

        # second line separator
        self.galaxy.add_entity(Line(self.galaxy,
                                    start_pos=[495, 20],
                                    end_pos=[495, 460],
                                    width=2))

        # cart panel
        self.cart_panel = CartPanel(self.galaxy,
                                rect=pygame.Rect(520, 15, 260, 460),
                                border_width=-1,
                                border_radius=3)
        self.galaxy.add_entity(self.cart_panel)

    def build_products_panel(self):
        # add products label
        products_label = Label(self.galaxy,
                               text='Selecione o produto: ' + self.selected_category_name.upper(),
                               text_alignment=LEFT,
                               rect=pygame.Rect(0, 0, 370, 25))
        self.products_panel.add_entity(products_label)
        self.galaxy.add_entity(products_label)

        # add product options
        for variant_value in self.inventory.product_name_set(self.selected_category_name):
            button = ProductButton(
                galaxy=self.galaxy,
                text=variant_value,
                action=self.product_pressed_event)
            self.products_panel.add_entity(button)
            self.galaxy.add_entity(button)

        if self.selected_product_name:
            # add separator
            separator = Label(self.galaxy,
                              text='',
                              text_alignment=LEFT,
                              rect=pygame.Rect(0, 0, 370, 5))
            self.products_panel.add_entity(separator)
            self.galaxy.add_entity(separator)

            # add weights label
            weights_label = Label(self.galaxy,
                                  text='Selecione o peso:',
                                  text_alignment=LEFT,
                                  rect=pygame.Rect(0, 0, 370, 25))
            self.products_panel.add_entity(weights_label)
            self.galaxy.add_entity(weights_label)

            # add weight options
            for variant_value in self.inventory.variant_value_set(self.selected_category_name, self.selected_product_name, 'peso'):
                button = ProductButton(
                    galaxy=self.galaxy,
                    text=variant_value,
                    action=self.weight_pressed_event)
                self.products_panel.add_entity(button)
                self.galaxy.add_entity(button)

            # add separator
            separator = Label(self.galaxy,
                              text='',
                              text_alignment=LEFT,
                              rect=pygame.Rect(0, 0, 370, 5))
            self.products_panel.add_entity(separator)
            self.galaxy.add_entity(separator)

            # add inclusions label
            inclusions_label = Label(self.galaxy,
                                     text='Selecione a inclusão (opcional):',
                                     text_alignment=LEFT,
                                     rect=pygame.Rect(0, 0, 370, 25))
            self.products_panel.add_entity(inclusions_label)
            self.galaxy.add_entity(inclusions_label)

            # add inclusion options
            for variant_value in self.inventory.variant_value_set(
                    self.selected_category_name, self.selected_product_name, 'inclusão'):
                button = ProductButton(
                    galaxy=self.galaxy,
                    text=variant_value,
                    action=self.inclusion_pressed_event)
                self.products_panel.add_entity(button)
                self.galaxy.add_entity(button)

    def rebuild_products_panel(self, category_name, product_name):
        for entity in self.products_panel.entities:
            entity.kill()
        self.products_panel.clear()
        self.selected_category_name = category_name
        self.selected_product_name = product_name
        self.build_products_panel()

    def category_pressed_event(self, button):
        self.rebuild_products_panel(button.text, None)

    def product_pressed_event(self, button):
        # if item in cart is not complete and you changed it,
        # removes and add the new one
        last_cart_item = self.cart_panel.last_cart_item()
        if last_cart_item and last_cart_item.product_name != button.text and \
                last_cart_item.weight_variant_value == '' or last_cart_item and \
                last_cart_item.category_name != self.selected_category_name and \
                last_cart_item.weight_variant_value == '':
            self.cart_panel.remove_entity(last_cart_item)  # remove from cart
            last_cart_item.kill()  # remove from galaxy
        self.cart_panel.rebuild()

        # If last item already in the cart is the same,
        # increment item count on cart
        if last_cart_item and last_cart_item.category_name == self.selected_category_name and \
                last_cart_item.product_name == button.text and \
                last_cart_item.weight_variant_value == '':
            last_cart_item.increment()
        # if not the same, add a new item to cart
        else:
            cart_button = CartButton(self.galaxy,
                                      category_name=self.selected_category_name,
                                      product_name=button.text,
                                      left_action=self.decrement_cart_item,
                                      right_action=self.increment_cart_item)
            self.cart_panel.add_entity(cart_button)
            self.galaxy.add_entity(cart_button)

            # re-build products pannel
            self.rebuild_products_panel(
                self.selected_category_name, button.text)

    def weight_pressed_event(self, button):
        cart_item = self.cart_panel.last_cart_item()
        if cart_item:
            variant = self.inventory.variant(
                self.selected_category_name, self.selected_product_name, 'peso', button.text)
            cart_item.update_weight_variant(variant['value'], variant['price'])
            self.cart_panel.rebuild()

    def inclusion_pressed_event(self, button):
        cart_item = self.cart_panel.last_cart_item()
        if cart_item:
            if cart_item.inclusion_variant_value != '' and cart_item.inclusion_variant_value == button.text:
                cart_item.update_inclusion_variant('', 0.)
            else:
                variant = self.inventory.variant(
                    self.selected_category_name, self.selected_product_name, 'inclusão', button.text)
                cart_item.update_inclusion_variant(
                    variant['value'], variant['price'])
            self.cart_panel.rebuild()

    def increment_cart_item(self, button):
        button.increment()
        self.cart_panel.rebuild()

    def decrement_cart_item(self, button):
        if button.quantity > 1:
            button.decrement()
        else:
            self.remove_from_cart(button)
        self.cart_panel.rebuild()

    def remove_from_cart(self, button):
        self.cart_panel.remove_entity(button)  # remove from cart
        button.kill()  # remove from galaxy
        self.cart_panel.rebuild()
