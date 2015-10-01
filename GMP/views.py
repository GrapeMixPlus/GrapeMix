from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.decorators import login_required



def inup(request):
    return render_to_response('grapemix.html')

def login(request):
    return render_to_response('login.html')

def logup(request):
    return render_to_response('logup.html')

@login_required
def home(request):
    return render_to_response('home.html')
