from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def emailsending(request):

    subject='hello this is test mail'
    message='test email from django'
    sendfrom='settings.EMAIL_HOST_USER'
    toaddress=['tomailaddress@gmail.com',]  #type the TO mail address here
    send_mail(subject,message,sendfrom,toaddress)
    return render(request,'index.html')