from django.shortcuts import render,redirect
from .utils import send_email_client
# Create your views here.

def send_email(request):
    send_email_client()
    return redirect("/")

def index(request):
    return render(request,'index.html')

