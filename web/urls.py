
from django.urls import path
import web.views as views

urlpatterns = [
    path('', views.home, name='home'),
]
