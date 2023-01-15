from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loging(request):
    return render(request,'login/login.html')