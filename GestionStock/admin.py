from django.contrib import admin

# Register your models here.
from GestionStock.models import Article, Rayon



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom_article','quantite','genre')

class RayonAdmin(admin.ModelAdmin):
    list_display = ('no_rayon','nombre_de_cellule','no_depot')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Rayon, RayonAdmin)
