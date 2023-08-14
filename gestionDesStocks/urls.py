
from django.contrib import admin
from django.urls import path
from GestionStock import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion-stock', views.afficher_articles),
]
