from django.http import HttpResponse
from django.shortcuts import render
from GestionStock.models import Article





def afficher_articles(request):
    articles = Article.objects.all()
    return render(request,
                  'afficher_articles.html',
                  {'articles': articles})




"""
def afficher_articles(request):
    articles = Article.objects.all()
    return HttpResponse(f '''
    <h1>Cette vue Fonctionne !!!</h1>
         <ul>
            <li>{articles[0].nom_article}, {articles[0].quantite}</li>
            <li>{articles[1].nom_article}, {articles[1].quantite}</li>
        </ul>
    ''')
"""