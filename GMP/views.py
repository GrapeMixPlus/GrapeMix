from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from GMP.models import Profile, Song, New, PlayList
from django.contrib import messages
import logging
import sys
logger = logging.getLogger('django')
import os
from django.http import HttpResponse
from GMP.forms import EditSocialProfileForm, MyUserCreationForm, UpSongForm


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
                Profile.objects.get_or_create(user=user)
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
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return redirect(reverse('GMP:home'))
    else:
        formulario = UserCreationForm()
    return render_to_response('logup.html',{'formulario':formulario}, context_instance=RequestContext(request))


    #return render_to_response('logup.html')

@login_required(login_url='/login')
def home(request):
    context = RequestContext(request)
    song = Song.objects.all()
    news = New.objects.all()
    listaplay = PlayList.objects.all()
    try:
        playlist=PlayList.objects.get(user=request.user)
        return render_to_response('home.html',{'songs': song,'playlist':playlist, 'news':news, 'listaplay':listaplay}, context)
    except:
        return render_to_response('home.html',{'songs': song, 'news':news}, context)



@login_required(login_url='/login')
def profile(request):
    args = {}
    context = RequestContext(request)
    try:
        user = request.user
    except User.DoesNotExist:
        raise Http404('El usuario no existe')

    if request.method == 'POST':
        form = EditSocialProfileForm(request.POST, request.FILES,
                instance=user.profile)

        if form.is_valid():
            logger.info(form.instance)
            form.save()
        if not user.profile.profile_photo:
            user.profile.profile_photo ='../multimedia/profile/profiledef.jpg'
            user.profile.save()
    else:
        form = EditSocialProfileForm(instance=user.profile)
    args['form'] = form
    return render(request, 'profile.html', args)



def song(request):
    args = {}
    context = RequestContext(request)
    song = Song()
    if request.method == 'POST':
        print >> sys.stderr, args
        formsong = UpSongForm(request.POST, request.FILES, instance=song)
        if formsong.is_valid():
            logger.info(formsong.instance)
            formsong.save()
    else:
        formsong = UpSongForm(instance=song)
    args['formsong'] = formsong
    return render(request, 'upsong.html', args)


def buscador(request, busqueda):
    context = RequestContext(request)
    songs = Song.objects.filter(tittle = busqueda)

    return render_to_response('lista.html',
                              {'songs':songs},
                              context)

def ver_new(request, id_new):
	context = RequestContext(request)
	the_new = New.objects.get(id=id_new)
	return render_to_response('new.html', {'mi_new':mi_new},context)

def addList(request):
    context = RequestContext(request)
    listas=PlayList.objects.all()
    lista=None
    for i in listas:
        if i.user == request.user:
            lista=i
            #lista=PlayList.objects.get(id=i.id)

    if lista == None:
        lista = PlayList()
        lista.name=str(request.user)+' list'
        lista.user=request.user
        lista.save()
    song = Song.objects.get(id=request.POST['id'])
    lista.song.add(song)
    return HttpResponse(status=202)

#def changelist(request):
#    context = RequestContext(request)
#    listas=PlayList.objects.get(id=request.POST['id'])
#    return render_to_response('home.html', {'listas':listas},context)
