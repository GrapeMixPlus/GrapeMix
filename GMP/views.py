from django.shortcuts import render_to_response, render, redirect

def inup(request):
    return render_to_response('grapemix.html')

def login(request):
    return render_to_response('login.html')

def logup(request):
    return render_to_response('logup.html')

def home(request):
    return render_to_response('home.html')
