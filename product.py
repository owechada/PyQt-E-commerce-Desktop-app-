import json

class Products:
    def __init__(self, image, title, price, description, id):
        self.image = image
        self.title = title
        self.price = price
        self.description = description
        self.id=id

    @classmethod
    def load_products_from_file(cls, file_path):
        products = []
        with open(file_path, 'r') as f:
            json_data = json.load(f)
        for item in json_data:
            product = cls(
                image=item.get('image'),
                title=item.get('title'),
                price=int(item.get('price')[3:].replace(",","")),
                description=item.get('description')
            )
            products.append(product)
        return products
    
    def get_details(self):
        return f"ID: {self.image}, Title: {self.title}, Price: {self.price}"

