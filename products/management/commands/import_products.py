import json
from django.core.management.base import BaseCommand
from products.models import Category, Vendor, Specifications, Product


class Command(BaseCommand):
    help = 'Import products into the database from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file containing scraped data')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            scraped_data = json.load(file)

        for data in scraped_data:
            category, _ = Category.objects.get_or_create(name=data['product_category'])
            vendor, _ = Vendor.objects.get_or_create(name=data['Brand_name'])
            specifications, _ = Specifications.objects.get_or_create(specifications=data['specifications'])

            # Create the product
            Product.objects.create(
                name=data['product_title'],
                price=data['price'].replace(',', ''),  # Remove commas for decimal field
                image_url=data['image_url'],
                category=category,
                vendor=vendor,
                specifications=specifications
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported products'))
