from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор статьи')
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Images(models.Model):
    image_name = models.CharField('Название изображения', max_length=50)
    image = models.ImageField()
    file = models.FileField()

    def __str__(self):
        return self.image_name

class Message(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор сообщения')
    text = models.TextField('Текст сообщения')
    timestamp = models.TimeField('Время отправки сообщения')

   # def __str__(self):
      #  return self.username

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
