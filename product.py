class Product():
    def __init__(self, name, category_name, variants):
        self.name = name
        self.category_name = category_name
        if not variants: self.variants = []
        else: self.variants = variants
