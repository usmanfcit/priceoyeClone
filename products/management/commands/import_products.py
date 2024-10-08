import json
from django.core.management.base import BaseCommand
from products.models import (
    Category,
    Vendor,
    SpecificationCategory,
    SpecificationDetail,
    ProductSpecificationCategory,
    Product
)


class Command(BaseCommand):
    help = "Import products into the database from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="Path to the JSON file containing scraped data")

    def handle(self, *args, **kwargs):
        json_file = kwargs["json_file"]

        with open(json_file, "r") as file:
            scraped_data = json.load(file)

        for product_data in scraped_data:
            category_name = product_data["product_category"].lower()
            vendor_name = product_data["Brand_name"].lower()

            category, _ = Category.objects.get_or_create(name=category_name)
            vendor, _ = Vendor.objects.get_or_create(name=vendor_name)

            product, _ = Product.objects.get_or_create(
                name=product_data["product_title"],
                price=product_data["price"].replace(",", ""),
                image_url=product_data["image_url"],
                category=category,
                vendor=vendor
            )

            for category_name, specs in product_data["specifications"].items():
                spec_category, _ = SpecificationCategory.objects.get_or_create(name=category_name)
                product_spec_category, _ = ProductSpecificationCategory.objects.get_or_create(
                    product=product,
                    specification_category=spec_category
                )
                for label_name, value in specs.items():

                    SpecificationDetail.objects.update_or_create(
                        specification_category=product_spec_category,
                        specification_label=label_name,
                        specification_value=value,
                        defaults={"specification_value": value}
                    )

        self.stdout.write(self.style.SUCCESS("Successfully imported products"))
