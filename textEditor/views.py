from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.
def home(request):
	return render(request,'textEditor/home.html')

@login_required
def textEditor(request):	
	return render(request,'textEditor/textEditor.html')
