from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
# Create your views here

class companylist(ListView):
    model=Company

class companydetail(DetailView):
    model=Company

class companycreateview(CreateView):
    model=Company
    fields=['name','location','ceo']

class companyupdateview(UpdateView):
    model=Company
    fields=['name','ceo']

class companydeleteview(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')