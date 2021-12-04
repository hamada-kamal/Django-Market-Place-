from django.shortcuts import render
# from django.core.mail import send_mail
# from django.conf import settings
from django.core.mail import EmailMessage
from .models import ContactInfo
from products.utils import CartData

def send_message(request):
    info = ContactInfo.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        emaill = EmailMessage(
        subject,
        message,
        email,
        ['hamadakamal819@gmail.com'],
        reply_to=[email],

        )

        emaill.send()
    data = CartData(request)
    cartItems = data['cartItems']
    return render(request,'pages/contact.html', {'info':info, 'cartItems': cartItems})