from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
# Create your views here.
def login(request):
    form = LoginForm()
    return render(request,'login.html',{'form':form})

def register(request):
    return HttpResponse('<h1>Register</h1>')