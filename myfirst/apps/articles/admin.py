from django.contrib import admin
from . models import Article, Comment, Images, Messages
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

admin.site.register(Images)
admin.site.register(Messages)
admin.site.register(Article)
admin.site.register(Comment)
