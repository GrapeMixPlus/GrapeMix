from django.contrib import admin

from GMP.models import Song, PlayList,Profile,New #,Artist
admin.site.register(Song)
admin.site.register(PlayList)
admin.site.register(Profile)
#admin.site.register(Artist)
admin.site.register(New)
