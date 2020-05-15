from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from . models import Article, Comment
from django.urls import reverse
from django.utils import timezone
import webbrowser

def index(request):
	latest_article_list = Article.objects.order_by('-pub_date')
	return render(request, 'articles/list.html', {'latest_article_list': latest_article_list})


def detail(request, article_id):
	try:
		a = Article.objects.get(id  = article_id)
	except:
		raise Http404("Статья не найдена")

	latest_comments_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list,})

def leave_comment(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		raise Http404("Статья не найдена")

	a.comment_set.create(author_name = request.POST['author_name'],
	comment_text = request.POST['comment_text'])

	return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )

def create_article(request):
	a = Article(
	article_title = request.POST['article_title'],
	article_text = request.POST['article_text'],
	pub_date = timezone.now())
	a.save()
	return HttpResponseRedirect('/articles/')

def calculator(request):
	return render(request, 'articles/calculator.html')
