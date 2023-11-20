from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tasks(request):
    return render(request,'tasks.html')
def salary(request):
    return render(request,'salary.html')
def updated(request):
    return HttpResponse('On process')

