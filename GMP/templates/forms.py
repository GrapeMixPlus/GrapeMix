
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, CharField
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from main.models import UserProfile, GENRE_CHOICES
from django.forms.utils import ErrorList
from main.widgets import MyFileInput
import logging

logger = logging.getLogger('django')

class MyUserCreationForm(UserCreationForm):
    error_css_class = 'alert alert-danger'
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for (field_name, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.widget.attrs['placeholder'] = 'Requerido'
                field.label = '* ' + str(field.label)
