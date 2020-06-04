from django.contrib import admin

# Register your models here.

from .models import Blog, Hashtag
admin.site.register(Blog)
admin.site.register(Hashtag)