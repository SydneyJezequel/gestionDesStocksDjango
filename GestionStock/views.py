from django.http import HttpResponse
from django.shortcuts import render, redirect
from GestionStock.models import Article, Rayon
from GestionStock.forms import addArticleForm


# Routage vers la page d'accueil :
def page_accueil(request):
  return render(request,'page_accueil.html')


# Affichage de la liste des Articles :
def afficher_articles(request):
    articles = Article.objects.all()
    return render(request,
                  'afficher_articles.html',
                  {'articles': articles})


#Affichage de la liste des rayons :
def afficher_rayons(request):
    rayons = Rayon.objects.all()
    return render(request,
                  'afficher_depots.html',
                  {'rayons': rayons})


# Affichage détaillé des Articles :
def article_detail(request, no_article):
  article = Article.objects.get(no_article=no_article)
  return render(request,
          'article_detail.html',
          {'article': article})


# Fonction pour ajouter un article :
def ajouter_article(request):
    # Exécution du formulaire de création :
    if request.method == 'POST':
        form = addArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion-stock')  # Redirige où vous le souhaitez après la création réussie
    # Echec de l'exécution du formulaire de création :
    else:
        form = addArticleForm()
    return render(request, 'ajouter_article.html', {'form': form})





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









