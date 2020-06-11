from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Article, Comment, Images, Messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import webbrowser
import time
import requests

messages = [
    {'username': 'Jack', 'text': 'Hello!', 'timestamp': time.time()}
]

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')
    return render(request, 'articles/list.html', {'latest_article_list': latest_article_list})


def detail(request, article_id):
    if request.user.is_authenticated:
        try:
            a = Article.objects.get(id=article_id)
        except:
            raise Http404("Статья не найдена")

        latest_comments_list = a.comment_set.order_by('-id')[:10]

        return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list, })
    else:
        return HttpResponseRedirect("/user/login/")


def leave_comment(request, article_id):
    if request.user.is_authenticated:
        try:
            a = Article.objects.get(id=article_id)
        except:
            raise Http404("Статья не найдена")

        a.comment_set.create(author_name=request.POST['author_name'],
                             comment_text=request.POST['comment_text'])

        return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
    else:
        return HttpResponseRedirect("/user/login/")


def create_article(request):
    if request.user.is_authenticated:
        a = Article(
            author=request.user,
            article_title=request.POST['article_title'],
            article_text=request.POST['article_text'],
            pub_date=timezone.now())
        a.save()
        # a.author = request.user
        return HttpResponseRedirect('/articles/')

    else:
        return HttpResponseRedirect("/user/login/")


def calculator(request):
    return render(request, 'articles/calculator.html')


def vitalik(request):
    all_images = Images.objects.order_by()[:1]
    return render(request, 'articles/lefort_and_not_only.html', {'all_images': all_images})


def register(request):
    return render(request, 'articles/register.html')


def create_user(request):
    user = User.objects.create_user(request.POST['username'], '', request.POST['password'])
    user.save()
    return HttpResponseRedirect("/user/login/")


def change_image(request):
    image = Images.objects.get(id=6)
    try:
        image.image_name = request.POST['change_image_name']
        image.image = request.FILES['photo']
        image.file = request.FILES['audio']
        image.save()
    except Exception:
        return HttpResponseRedirect("/vitalik/")
    return HttpResponseRedirect("/vitalik/")

def send_message(request):
    if (len(request.POST['text_message']) < 1) == False :
        message = Messages(
        #username=request.user,
        text=request.POST['text_message'],
        timestamp= timezone.now())
        message.save()
        return HttpResponseRedirect('/chat/')
    else:
        return HttpResponseRedirect('/chat/')


def chat(request):
    messages = Messages.objects.all()
    return render(request, 'messenger/index.html', {'messages': messages})