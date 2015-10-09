from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from GMP.models import UserProfile
import logging
logger = logging.getLogger('django')

class DivErrorList(ErrorList):
    def __unicode__(self): # __unicode__ on Python 2
        return self.as_divs()
    def as_divs(self):
        if not self:
            return ''
        return '<div class="alert alert-danger">%s</div>' \
    % ''.join(['<div class="alert-danger">%s</div>' % e
               for e in self])

class MyUserCreationForm(UserCreationForm):
    error_css_class = 'alert alert-danger'
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for (field_name, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.widget.attrs['placeholder'] = 'Requerido'
                field.label = '* ' + str(field.label)


