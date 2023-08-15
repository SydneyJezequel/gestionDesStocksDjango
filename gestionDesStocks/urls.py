
from django.contrib import admin
from django.urls import path
from GestionStock import views


urlpatterns = [
    path('', views.page_accueil),
    path('admin/', admin.site.urls),
    path('ajouter-article/', views.ajouter_article, name='ajouter-article'),
    path('gestion-stock/', views.afficher_articles, name='gestion-stock'),
    path('gestion-rayons/', views.afficher_rayons, name='gestion-rayons'),
    path('articles/<int:no_article>/', views.article_detail, name='article-detail')
]
