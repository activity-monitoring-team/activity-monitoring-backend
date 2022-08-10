from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Orders, BaseModel
from datetime import datetime
from .forms import LoginForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.utils import timezone
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView



def home(request):


    


    if request.method == 'GET':
        return render(request, 'auth.html')
    

def index(request):
    orders = Orders.objects.all()
    context = {
        'orders': orders
    }
    template = 'index.html'
    return render(request, template, context)

class UserLogin(LoginView):
     template = 'auth.html'
     form_class = LoginForm
     succes_url = reverse_lazy('index')
     def get_success_url(self) -> str:
         return self.succes_url

class UserLogOut(LogoutView):
     next_page = reverse_lazy('login_page')
