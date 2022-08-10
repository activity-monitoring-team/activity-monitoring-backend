from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Orders, BaseModel
from datetime import datetime
#from .forms import OrdersForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.utils import timezone
from datetime import datetime



def home(request):


    orders = Orders.objects.all()


    if request.method == 'GET':
        return render(request, 'index.html', {'orders': orders})
    

#def index(request):
   

    
   # form = OrdersForm()

    #data = {
    #    'form': form
   # }

    #return render(request, 'index.html', data)

  #  elif request.method == 'POST':
   #     return redirect ('index')