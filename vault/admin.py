from django.contrib import admin
from .models import Mainslide,Video,Article,Weeksuggestions,Animes,Movie,Series

# Register your models here.
admin.site.register(Video)
admin.site.register(Article)
admin.site.register(Weeksuggestions)
admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(Animes)
admin.site.register(Mainslide)