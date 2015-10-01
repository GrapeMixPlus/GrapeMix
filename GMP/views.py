from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from GMP.forms import MyUserCreationForm
from django.template import RequestContext
from django.contrib.auth.models import User


def inup(request):
    return render_to_response('grapemix.html')

def login(request):
    context = RequestContext(request)

    createUserForm = MyUserCreationForm()
    args = {}
    args['createUserForm'] = createUserForm

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
                                     'Invalid User')
                return render_to_response('login.html', args, context)
        else:
            messages.add_message(request, messages.ERROR,
                                 'Invalid User')
            return render_to_response('login.html', args, context)
    else:
        return render_to_response('login.html',args, context)

def logup(request):
    return render_to_response('logup.html')

@login_required(login_url='/login')
def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)
