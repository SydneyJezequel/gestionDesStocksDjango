from django.contrib import admin

# Register your models here.
from GestionStock.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom_article','quantite','genre')

admin.site.register(Article, ArticleAdmin)
