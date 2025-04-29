from django.utils import timezone
from django.db import models
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(u'Категорія',
                                max_length=250, help_text=u'Максимум 250 сим.')
    slug = models.SlugField(u'Слаг')
    objects = models.Manager()

    class Meta:
        verbose_name = u'Категорія для публікації'
        verbose_name_plural = u'Категорії для публікацій'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse('articles-category-list',
                          kwargs={'slug': self.slug})
        except:
            url = "/"
        return url


# Модель для публікацій блогу
class Article(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    description = models.TextField(blank=True, verbose_name='Опис')
    pub_date = models.DateTimeField('Дата публікації', default=timezone.now)
    slug = models.SlugField('Слаг', unique_for_date='pub_date')
    main_page = models.BooleanField('Головна', default=False)
    category = models.ForeignKey(
        Category, 
        related_name='articles', 
        blank=True, 
        null=True, 
        verbose_name='Категорія', 
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Публікація'
        verbose_name_plural = 'Публікації'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={
            'year': self.pub_date.year,
            'month': self.pub_date.month,
            'day': self.pub_date.day,
            'slug': self.slug
        })

# Модель для зображень, що пов'язані з публікацією
class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('Фото', upload_to='photos')
    title = models.CharField('Заголовок', max_length=250, blank=True)

    class Meta:
        verbose_name = 'Фото для статті'
        verbose_name_plural = 'Фото для статті'

    def __str__(self):
        return self.title
