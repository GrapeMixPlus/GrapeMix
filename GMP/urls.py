from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'GMP.views.inup', name='inup'),
                       url(r'^home/$', "GMP.views.home", name='home'),
                       url(r'^login/$', "GMP.views.login", name='login'),
                       url(r'^logup/$', "GMP.views.logup", name='logup'),
                      )
