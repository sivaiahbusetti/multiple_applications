from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def projects(request):
    return render(request,'projects.html')
def employes(request):
    return render(request,'employes.html')
def countPrj(request):
    return HttpResponse('count is 20')