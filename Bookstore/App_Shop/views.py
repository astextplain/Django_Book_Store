

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from App_Shop.models import product
from  django.views.generic import ListView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
#Using Function based view
class Home(ListView):
    model=product
    template_name='App_Shop/home.html'

class productDetail(LoginRequiredMixin,DeleteView):
    model=product
    template_name='App_Shop/product_detail.html'






