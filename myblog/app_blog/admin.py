from django.contrib import admin
from .models import Category, Article, ArticleImage

# Клас для налаштування вигляду категорій в адмінці
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}  # Автоматичне створення слага з категорії

admin.site.register(Category, CategoryAdmin)

# Клас для налаштування вигляду зображень статей в адмінці
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1  # Дозволяє додавати додаткові зображення до публікації
    fields = ('image', 'title')  # Поля, які будуть доступні для редагування в адмінці

# Клас для налаштування вигляду статей в адмінці
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    list_filter = ('category', 'main_page')  # Додано фільтрацію за категорією та головною сторінкою
    search_fields = ('title', 'description')  # Додано пошук по заголовку та опису
    prepopulated_fields = {'slug': ('title',)}  # Автоматичне створення слага з заголовку
    raw_id_fields = ('category',)  # Використовуємо raw_id_field для полегшення вибору категорії
    inlines = [ArticleImageInline]  # Додаємо вбудовані зображення для статей

admin.site.register(Article, ArticleAdmin)

# Реєстрація ArticleImage для можливості редагування зображень в адмінці
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'article', 'image')  # Відображаємо назву, статтю та зображення
    search_fields = ('title',)  # Додаємо пошук по заголовку

admin.site.register(ArticleImage, ArticleImageAdmin)
