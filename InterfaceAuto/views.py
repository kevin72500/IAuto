from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
def login(request):
	return render(request,'InterfaceAuto/login.html')
def signup(request):
	return render(request,'InterfaceAuto/signup.html')
def index(request):
	return render(request,'InterfaceAuto/index.html')