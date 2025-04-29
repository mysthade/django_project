from django.utils import timezone
from django.db import models
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(u'Категорія', max_length=250)
    slug = models.SlugField(u'Слаг')

    class Meta:
        verbose_name = u'Категорія для публікації'
        verbose_name_plural = u'Категорії для публікацій'

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(u'Заголовок', max_length=250)
    description = models.TextField(blank=True, verbose_name=u'Опис')
    pub_date = models.DateTimeField(u'Дата публікації', default=timezone.now)
    slug = models.SlugField(u'Слаг', unique_for_date='pub_date')
    main_page = models.BooleanField(u'Головна', default=False)
    category = models.ForeignKey(Category, related_name='articles', blank=True, null=True, verbose_name=u'Категорія', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = u'Публікація'
        verbose_name_plural = u'Публікації'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'day': self.pub_date.day, 'slug': self.slug})

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(u'Фото', upload_to='photos')
    title = models.CharField(u'Заголовок', max_length=250, blank=True)

    class Meta:
        verbose_name = u'Фото для статті'
        verbose_name_plural = u'Фото для статті'

    def __str__(self):
        return self.title
