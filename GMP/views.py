from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from GMP.models import UserProfile
from GMP.forms import MyUserCreationForm
from django.contrib import messages
import logging
logger = logging.getLogger('django')
import os

def inup(request):
    return render_to_response('grapemix.html')

def log_out(request):
    logout(request)
    context = RequestContext(request)
    messages.add_message(request, messages.SUCCESS, 'Muchas gracias!')
    return redirect('/')

def log_in(request):
    context = RequestContext(request)

    #createUserForm = MyUserCreationForm()
    args = {}
    #args['createUserForm'] = createUserForm

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/home')
            else:
                messages.add_message(request, messages.ERROR,
                                     'El usuario no esta activo')
                return render_to_response('login.html', args, context)
        else:
            messages.add_message(request, messages.ERROR,
                                 'Invalid User')
            return render_to_response('login.html', args, context)
    else:
        return render_to_response('login.html',args, context)

def logup(request):
    context = RequestContext(request)
    createUserForm = MyUserCreationForm()
    args = {}
    args['createUserForm'] = createUserForm

    if request.method =='POST':
        createUserForm = MyUserCreationForm(request.POST)
        if createUserForm.is_valid():
            userform = createUserForm.save()
            userform.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, userform)
            return redirect('/')
        else:
            createUserForm = MyUserCreationForm()
            args['createUserForm'] = createUserForm
            return render_to_response('login.html', args, context)

@login_required(login_url='/login')
def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)
