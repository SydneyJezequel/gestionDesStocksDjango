from django.contrib import admin
from django.urls import path
from GestionStock import views




# Liste des urls de l'application :
urlpatterns = [
    path('', views.page_accueil),
    path('admin/', admin.site.urls),
    path('ajouter-article/', views.ajouter_article, name='ajouter-article'),
    path('gestion-stock/', views.afficher_articles, name='gestion-stock'),
    path('gestion-rayons/', views.afficher_rayons, name='gestion-rayons'),
    path('gestion-depots/', views.afficher_depots, name='gestion-depots'),
    path('ajouter-depot/', views.ajouter_depot_adresse, name='ajouter-depot'),
    path('ajouter-rayon/', views.ajouter_rayon, name='ajouter-rayon'),
    path('articles/<int:no_article>/', views.article_detail, name='article-detail'),
    path('supprimer-depot/<int:no_depot>/', views.supprimer_depot, name='supprimer-depot'),
    path('supprimer-article/<int:no_article>/', views.supprimer_article, name='supprimer-article'),
    path('supprimer-rayon/<int:no_rayon>/', views.supprimer_rayon, name='supprimer-rayon')
]



