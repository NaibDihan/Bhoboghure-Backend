from django.shortcuts import render,redirect
from  django.http import JsonResponse

# Create your views here.
from .models import Customer
from .forms import CustomerForm



def index(request):
    customers_list = Customer.objects.all()
    context = {'customers_list': customers_list}
    return render(request,'/home/index.html',context=context)