from product import Product
from ordered_set import OrderedSet


class Inventory():
    def __init__(self):
        self.product_list = [

            ###### BARRAS #####

            Product('100%', 'Barra', (
                {'name': 'peso', 'value': '15g', 'price': 5.},
                {'name': 'peso', 'value': '18g', 'price': 6.},
                {'name': 'peso', 'value': '50g', 'price': 15.},
                {'name': 'peso', 'value': '80g', 'price': 22.},
                {'name': 'peso', 'value': '100g', 'price': 27.},
            )),
            Product('80%', 'Barra', (
                {'name': 'peso', 'value': '15g', 'price': 5.},
                {'name': 'peso', 'value': '18g', 'price': 6.},
                {'name': 'peso', 'value': '50g', 'price': 15.},
                {'name': 'peso', 'value': '80g', 'price': 22.},
                {'name': 'peso', 'value': '100g', 'price': 27.},
                {'name': 'inclusão', 'value': 'Nuts', 'price': 0.},
                {'name': 'inclusão', 'value': 'Nibs', 'price': 0.},
            )),
            Product('70%', 'Barra', (
                {'name': 'peso', 'value': '15g', 'price': 5.},
                {'name': 'peso', 'value': '50g', 'price': 15.},
                {'name': 'peso', 'value': '80g', 'price': 22.},
                {'name': 'peso', 'value': '100g', 'price': 27.},
                {'name': 'inclusão', 'value': 'Nuts', 'price': 0.},
            #     {'name': 'inclusão', 'value': 'Café', 'price': 0.},
            )),
            Product('55%', 'Barra', (
                {'name': 'peso', 'value': '15g', 'price': 5.},
                {'name': 'peso', 'value': '18g', 'price': 6.},
                {'name': 'peso', 'value': '50g', 'price': 15.},
                {'name': 'peso', 'value': '80g', 'price': 22.},
                {'name': 'peso', 'value': '100g', 'price': 27.},
            #     {'name': 'inclusão', 'value': 'Nuts', 'price': 0.},
            #     {'name': 'inclusão', 'value': 'Pistache', 'price': 0.},
                {'name': 'inclusão', 'value': 'Amendoim', 'price': 0.},
            )),
            Product('52%', 'Barra', (
                {'name': 'peso', 'value': '15g', 'price': 5.},
                {'name': 'peso', 'value': '50g', 'price': 15.},
            )),
            # Product('50%', 'Barra', (
            #     {'name': 'peso', 'value': '15g', 'price': 5.},
            #     {'name': 'peso', 'value': '18g', 'price': 6.},
            #     {'name': 'peso', 'value': '50g', 'price': 15.},
            #     {'name': 'peso', 'value': '80g', 'price': 22.},
            #     {'name': 'peso', 'value': '100g', 'price': 27.},
            #     {'name': 'inclusão', 'value': 'Hibisco', 'price': 0.},
            #     {'name': 'inclusão', 'value': 'Nuts', 'price': 0.},
            #     {'name': 'inclusão', 'value': 'Pistache', 'price': 0.},
            #     {'name': 'inclusão', 'value': 'Amendoim', 'price': 0.},
            #     {'name': 'inclusão', 'value': 'Damasco', 'price': 0.},
            #     {'name': 'inclusão', 'value': 'Berries', 'price': 0.},
            # )),
            Product('Branco', 'Barra', (
                {'name': 'peso', 'value': '15g', 'price': 5.},
                {'name': 'peso', 'value': '18g', 'price': 6.},
                {'name': 'peso', 'value': '50g', 'price': 15.},
                {'name': 'peso', 'value': '80g', 'price': 22.},
                {'name': 'peso', 'value': '100g', 'price': 27.},
                {'name': 'inclusão', 'value': 'Pistache', 'price': 0.},
                {'name': 'inclusão', 'value': 'Damasco', 'price': 0.},
                {'name': 'inclusão', 'value': 'Berries', 'price': 0.},
            )),
            Product('Cupulate', 'Barra', (
                {'name': 'peso', 'value': '15g', 'price': 5.},
                {'name': 'peso', 'value': '50g', 'price': 15.},
                {'name': 'peso', 'value': '80g', 'price': 22.},
                {'name': 'peso', 'value': '100g', 'price': 27.},
                {'name': 'inclusão', 'value': 'Berries', 'price': 0.},
                {'name': 'inclusão', 'value': 'Nibs', 'price': 0.},
            #     {'name': 'inclusão', 'value': 'Damasco', 'price': 0.},
            )),

            # ##### OVOS #####

            # Product('70%', 'Ovo', (
            #     {'name': 'peso', 'value': '100g', 'price': 30.},
            #     {'name': 'peso', 'value': '250g', 'price': 75.},
            # )),
            # Product('55%', 'Ovo', (
            #     {'name': 'peso', 'value': '100g', 'price': 30.},
            #     {'name': 'peso', 'value': '250g', 'price': 75.},
            # )),
            # Product('Branco', 'Ovo', (
            #     {'name': 'peso', 'value': '100g', 'price': 30.},
            #     {'name': 'peso', 'value': '250g', 'price': 75.},
            #     {'name': 'inclusão', 'value': 'Berries', 'price': 0.},
            # )),

            # ##### BOMBONS #####

            # Product('70%', 'Bombom', (
            #     {'name': 'peso', 'value': '8g', 'price': 3.},
            #     {'name': 'peso', 'value': '10g', 'price': 3.},
            #     {'name': 'peso', 'value': '12g', 'price': 7.},
            #     {'name': 'inclusão', 'value': 'Amêndoas', 'price': 0.},

            # )),
            # Product('55%', 'Bombom', (
            #     {'name': 'peso', 'value': '8g', 'price': 3.},
            #     {'name': 'peso', 'value': '10g', 'price': 3.},
            #     {'name': 'peso', 'value': '12g', 'price': 7.},
            # )),
            Product('Branco', 'Bombom', (
                # {'name': 'peso', 'value': '8g', 'price': 3.},
                # {'name': 'peso', 'value': '10g', 'price': 3.},
                {'name': 'peso', 'value': '15g', 'price': 5.},
                {'name': 'inclusão', 'value': 'Hibisco', 'price': 0.},
                # {'name': 'inclusão', 'value': 'Berries', 'price': 0.},
            )),
            # Product('Cupulate', 'Bombom', (
            #     {'name': 'peso', 'value': '8g', 'price': 3.},
            #     {'name': 'peso', 'value': '10g', 'price': 3.},
            #     {'name': 'peso', 'value': '12g', 'price': 7.},
            #     {'name': 'inclusão', 'value': 'Berries', 'price': 0.},
            # )),

            ##### CREME DE AVELÃ #####

            Product('Nuvega', 'Avelã', (
                {'name': 'peso', 'value': '120g', 'price': 27.},
                {'name': 'peso', 'value': '40g', 'price': 12.},
            )),

            # ##### PASTA DE AMENDOIM #####

            # Product('Bunnoim', 'Amendoim', (
            #     {'name': 'peso', 'value': '120g', 'price': 26.},
            #     {'name': 'peso', 'value': '40g', 'price': 12.},
            # )),
        ]

    def category_name_set(self):
        category_name_list = []
        for product in self.product_list:
            category_name_list.append(product.category_name)
        return OrderedSet(category_name_list)

    def product_name_set(self, category_name):
        name_list = []
        for product in self.product_list:
            if product.category_name == category_name:
                name_list.append(product.name)
        return OrderedSet(name_list)

    def variant_name_set(self, category_name, product_name):
        variant_names = []
        for product in self.product_list:
            if product.category_name == category_name and product.name == product_name:
                for variant in product.variants:
                    variant_names.append(variant['name'])
        return OrderedSet(variant_names)

    def variant_value_set(self, category_name, product_name, variant_name):
        variant_values = []
        for product in self.product_list:
            if product.category_name == category_name and product.name == product_name:
                for variant in product.variants:
                    if variant['name'] == variant_name:
                        variant_values.append(variant['value'])
        return OrderedSet(variant_values)

    def variant(self, category_name, product_name, variant_name, variant_value):
        for product in self.product_list:
            if product.category_name == category_name and product.name == product_name:
                for variant in product.variants:
                    if variant['name'] == variant_name and variant['value'] == variant_value:
                        return variant


if __name__ == "__main__":
    # exemplos
    inventory = Inventory()
    print(inventory.category_name_set())
    print(inventory.product_name_set('Ovo'))
    print(inventory.variant_name_set('Ovo', 'Branco'))
    print(inventory.variant_value_set('Ovo', 'Branco', 'peso'))
    print(inventory.variant_value_set('Ovo', 'Branco', 'inclusão'))
    print(inventory.product_name_set('Barra'))
    print(inventory.variant_name_set('Barra', 'Branco'))
    print(inventory.variant_value_set('Barra', 'Branco', 'peso'))
    print(inventory.variant_value_set('Barra', 'Branco', 'inclusão'))
    print(inventory.variant('Barra', 'Branco', 'peso', '50g'))
        