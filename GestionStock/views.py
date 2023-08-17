from django.shortcuts import render, redirect
from GestionStock.models import Article, Rayon, Depot
from GestionStock.forms import addArticleForm, addDepotForm




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
                  'afficher_rayons.html',
                  {'rayons': rayons})




# Affichage détaillé des Articles :
def article_detail(request, no_article):
  article = Article.objects.get(no_article=no_article)
  return render(request,
          'article_detail.html',
          {'article': article})




# Fonction qui gère la vue et le formulaire pour ajouter un article :
def ajouter_article(request):
    # Exécution du formulaire de création :
    if request.method == 'POST':
        form = addArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article-detail', article.no_article)  # Redirige où vous le souhaitez après la création réussie
    # Echec de l'exécution du formulaire de création :
    else:
        form = addArticleForm()
    return render(request, 'ajouter_article.html', {'form': form})




#Affichage de la liste des Dépôts
def afficher_depots(request):
    depots = Depot.objects.all()
    return render(request,
                  'afficher_depots.html',
                  {'depots': depots})




# Fonction qui gère la vue et le formulaire pour ajouter un dépôt :
def ajouter_depot(request):
    # Exécution du formulaire de création :
    if request.method == 'POST':
        form = addDepotForm(request.POST)
        if form.is_valid():
            depot = form.save()
            return redirect('gestion-depots')  # Redirige où vous le souhaitez après la création réussie
    # Echec de l'exécution du formulaire de création :
    else:
        form = addDepotForm()
    return render(request, 'ajouter_depot.html', {'form': form})



