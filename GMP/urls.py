from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^blog/$', "GMP.views.home", name='blog'),
                       url(r'^cont/$', "GMP.views.cont", name='cont'),
                      )
