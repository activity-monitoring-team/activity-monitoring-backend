from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Projects, Clients

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags

def home(request):

    context = {}
    projects = Projects.objects.all()
    context['projects'] = projects

    if request.method == 'GET':
        return render(request, 'index.html', context)
        
    elif request.method == 'POST':
        data = request.POST
        name = data['name']
        email = data['email']
        phone = data['phone']
        telegram = data['telegram']
        message = data['message']
        lang = data['lang']
        
        clients = Clients(name = name, email = email, phone = phone, telegram = telegram, message = message, lang = lang)
        clients.save()

        subject = name
        plain_message = 'почта: ' + email + '\nтелефон: ' + phone + '\nтелеграм: ' + telegram + '\nсообщение: ' + message + '\nязык: ' + lang
        from_email = settings.EMAIL_HOST_USER
        to = 'tima251+ibaoghxnkxgkquvv3uh3@boards.trello.com'


        try:
            send_mail(subject, plain_message, from_email, [to])
            print('mail successfully send')
            context['status'] = 1
            return render(request, 'index.html', context)

        except:
            print('error send mail')
            context['status'] = 0
            return render(request, 'index.html', context)
