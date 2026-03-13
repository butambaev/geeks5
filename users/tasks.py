from celery import shared_task
import random
from product.models import Product
from django.core.mail import send_mail


@shared_task
def generate_random_number():
    number = random.randint(1000, 9999)
    print(f"Generated number: {number}")
    return number


@shared_task
def delete_products_without_stock():
    products = Product.objects.filter(in_stock=0)
    count = products.count()
    products.delete()

    print(f"Deleted {count} products")


@shared_task
def send_test_email(email):

    send_mail(
        "Test email",
        "This is a test email from Celery",
        "your_email@gmail.com",
        [email],
        fail_silently=False,
    )

    print(f"Email sent to {email}")