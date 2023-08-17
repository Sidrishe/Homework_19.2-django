from django.core.management import BaseCommand
import json
from catalog.models import Product, Category
from config.settings import BASE_DIR


class Command(BaseCommand):
    filename = f'{BASE_DIR}\data.json'

    @staticmethod
    def read_json():
        with open(Command.filename, 'r', encoding='utf-8') as file:
            product_list = json.load(file)
        return product_list

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()

        create_product = []
        for product in Command.read_json():
            create_product.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'])
            )

        Product.objects.bulk_create(create_product)
