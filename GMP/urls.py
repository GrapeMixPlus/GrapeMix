from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'GMP.views.inup', name='inup'),
                       url(r'^home/$', "GMP.views.home", name='home'),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name':'login.html'}, name='login'),
                       url(r'^out/$' , 'django.contrib.auth.views.logout_then_login',
                           name='logout'),
                       url(r'^logup/$', "GMP.views.logup", name='logup'),
                      )
