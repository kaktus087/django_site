from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('articles/', views.index, name='index'),
    path('articles/<int:article_id>/', views.detail, name='detail'),
    path('articles/<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('articles/create_article/', views.create_article, name='create_article'),
    path('calculator/', views.calculator, name='calculator'),
    path('vitalik/', views.vitalik, name='vitalik'),
    path('registration/', views.register, name='register'),
    path('registration/create_user/', views.create_user, name='create_user'),
    path('vitalik/change_image/', views.change_image, name='change_image'),
   	path('send_message/', views.send_message, name='send_message'),
    path('chat/', views.chat, name='chat'),
    path('get_messages/', views.get_messages, name='get_messages'),
]
