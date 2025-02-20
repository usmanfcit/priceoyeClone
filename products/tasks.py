import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from celery import shared_task
from django.conf import settings

from products.models import Product

DOWNLOAD_DIR = os.path.join(settings.BASE_DIR, 'downloaded_images')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_image(image_url, save_as):
    try:
        urllib.request.urlretrieve(image_url, save_as)
        return True, None
    except Exception as e:
        return False, str(e)


@shared_task
def download_and_save_images_in_bulk():
    products = Product.objects.all()
    updates = []

    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = []
        for product in products:
            image_url = product.image_url.replace(" ", "%20")
            print("Downloading", image_url)
            image_name = image_url.split("/")[-1]
            save_as = os.path.join(DOWNLOAD_DIR, image_name)
            future = executor.submit(download_image, image_url, save_as)
            futures.append((future, product, image_name))

        for future, product, image_name in futures:
            success, error_message = future.result()
            if success:
                product.image = f"downloaded_images/{image_name}"
                updates.append(product)

    if updates:
        Product.objects.bulk_update(updates, ['image'])

    return f"Successfully downloaded and updated images for {len(updates)} products."
