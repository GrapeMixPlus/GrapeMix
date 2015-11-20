from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'GMP.views.inup', name='inup'),
                       url(r'^home/$', "GMP.views.home", name='home'),
                       url(r'^login/$', 'GMP.views.log_in', name='login'),
                       url(r'^out/$' , 'GMP.views.log_out', name='logout'),
                       url(r'^logup/$', "GMP.views.logup", name='logup'),
                       url(r'^profile/$', "GMP.views.profile", name='profile'),
                       url(r'^upsong/$', "GMP.views.song", name='upsong'),
                       url(r'^song_list/$', "GMP.views.song_list", name='song_list'),
                      )
