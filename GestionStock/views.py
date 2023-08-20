# Dépendances :
from django.shortcuts import render, redirect
from GestionStock.models import Article, Rayon, Depot
from GestionStock.forms import addArticleForm, addAdresseForm, addDepotFormSet, addRayonForm








# ************************************* Vues princ ************************************* #




# Routage vers la page d'accueil :
def page_accueil(request):
  return render(request, 'page_accueil.html')




# Affichage de la liste des Articles :
def afficher_articles(request):
    articles = Article.objects.all()
    return render(request,
                  'afficher_articles.html',
                  {'articles': articles})




# Affichage de la liste des rayons :
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




# Affichage de la liste des Dépôts
def afficher_depots(request):
    depots = Depot.objects.all()
    return render(request,
                  'afficher_depots.html',
                  {'depots': depots})










# ************************************* Formulaires d'ajout ************************************* #




# Formulaire pour ajouter un article :
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




# Formulaire pour ajouter un dépôt et son adresse :
def ajouter_depot_adresse(request):
    # Exécution du formulaire de création :
    if request.method == 'POST':
        adresse_form = addAdresseForm(request.POST)
        depot_formset = addDepotFormSet(request.POST, prefix='depot')
        if adresse_form.is_valid() and depot_formset.is_valid():
            adresse = adresse_form.save()
            for depot_form in depot_formset:
                depot = depot_form.save(commit=False)
                depot.no_adresse = adresse
                depot.save()
            return redirect('gestion-depots')  # Redirige où vous le souhaitez après la création réussie
    # Echec de l'exécution du formulaire de création :
    else:
        adresse_form = addAdresseForm()
        depot_formset = addDepotFormSet(prefix='depot')
    return render(request, 'ajouter_depot.html', {'adresse_form': adresse_form, 'depot_formset': depot_formset})




# Formulaire pour ajouter un rayon et son dépôt :
def ajouter_rayon(request):
    # Exécution du formulaire de création :
    if request.method == 'POST':
        form = addRayonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion-rayons')  # Redirige où vous le souhaitez après la création réussie
    # Echec de l'exécution du formulaire de création :
    else:
        form = addRayonForm()
    return render(request, 'ajouter_rayon.html', {'form': form})





