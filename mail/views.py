from django.shortcuts import render, redirect
from .forms import *
from django.core.mail import send_mail


def mailing(request):
    form = MailForm()
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, email, [email])
        return render(request, template_name='mail/send.html')
    context = {'form': form}
    return render(request, 'mail/mailing.html', context)

