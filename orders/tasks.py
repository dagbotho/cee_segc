from celery import shared_task
from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an email notification when a new order is created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id} created'
    message = f'Dear {order.first_name},\n\n' \
              f'Your order has been successfully created.\n' \
              f'Order ID: {order.id}\n' \
              f'Thank you for your purchase!'
    
    mail_sent = send_mail(subject, message, 'admin@cee_segc.com',
                          [order.email])
    return mail_sent