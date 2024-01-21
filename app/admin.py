from django.contrib import admin
from .models import movie,comments
# Register your models here.

class movieadmin(admin.ModelAdmin):
    list_display=['title','blog_date','release_date','movie_rating']

class commentadmin(admin.ModelAdmin):
    list_display=['user','comment_date','comment','user_rating']


admin.site.register(movie,movieadmin)
admin.site.register(comments,commentadmin)
