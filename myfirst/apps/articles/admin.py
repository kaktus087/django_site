from django.contrib import admin
from . models import Article, Comment
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()
admin.site.register(Article)
admin.site.register(Comment)
