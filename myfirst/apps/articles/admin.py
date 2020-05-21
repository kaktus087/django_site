from django.contrib import admin
from . models import Article, Comment, Images
from django.contrib.admin.models import LogEntry

admin.site.register(Images)
LogEntry.objects.all().delete()
admin.site.register(Article)
admin.site.register(Comment)
