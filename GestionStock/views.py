# Dépendances :
from django.shortcuts import render, redirect, get_object_or_404
from GestionStock.models import Article, Rayon, Depot, Adresse
from GestionStock.forms import AdresseEditForm, DepotEditForm, ArticleEditForm, RayonEditForm, addArticleForm, \
    addAdresseForm, addDepotFormSet, addRayonForm, depotEditFormSet


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










# ************************************* Méthodes de suppression ************************************* #




# Méthode de suppression d'un dépôt :
def supprimer_depot(request, no_depot):
    depot = get_object_or_404(Depot, no_depot=no_depot)

    if request.method == 'POST':
        depot.delete()
        return redirect('gestion-depots')

    return render(request, 'supprimer_depot.html', {'depot': depot})




# Méthode de suppression d'un article :
def supprimer_article(request, no_article):
    article = get_object_or_404(Article, no_article=no_article)

    if request.method == 'POST':
        article.delete()
        return redirect('gestion-stock')

    return render(request, 'supprimer_article.html', {'article': article})




# Méthode de suppression d'un rayon :
def supprimer_rayon(request, no_rayon):
    rayon = get_object_or_404(Rayon, no_rayon=no_rayon)

    if request.method == 'POST':
        rayon.delete()
        return redirect('gestion-rayons')

    return render(request, 'supprim_rayon.html', {'rayon': no_rayon})










# ************************************* Formulaires d'Edition ************************************* #




# Formulaire d'édition d'un dépot :
def edition_depot_adresse(request, no_depot):
    depot = get_object_or_404(Depot, pk=no_depot)
    adresse = depot.no_adresse

    if request.method == 'POST':
        editAdressForm = AdresseEditForm(request.POST, instance=adresse)
        editDepotForm = DepotEditForm(request.POST, instance=depot)

        if editAdressForm.is_valid() and editDepotForm.is_valid():
            adresse = editAdressForm.save()
            depot = editDepotForm.save(commit=False)
            depot.no_adresse = adresse
            depot.save()
            # Rediriger vers une autre vue ou effectuer d'autres actions
            return redirect('gestion-depots')
    else:
        editAdressForm = AdresseEditForm(instance=adresse)
        editDepotForm = DepotEditForm(instance=depot)

    return render(request, 'edition_depot.html',
                  {'editDepotForm': editDepotForm, 'editAdressForm': editAdressForm, 'depot': depot})



# CORRECTION : VERSION DU CODE 2 :
"""
def edition_depot_adresse(request, no_depot):
    depot = get_object_or_404(Depot, pk=no_depot)
    # LIGNE A CORRIGER :
    # adresse = Adresse.objects.get(pk=depot.no_adresse_id)
    adresse = depot.no_adresse

    if request.method == 'POST':
        editAdressForm = AdresseEditForm(request.POST, instance=adresse)
        depot_edit_formset = depotEditFormSet(request.POST, instance=depot)
        if editAdressForm.is_valid() and depot_edit_formset.is_valid():
            adresse = editAdressForm.save()
            for depot_form in depot_edit_formset:
                depot = depot_form.save(commit=False)
                depot.no_adresse = adresse
                depot.save()
            # Rediriger vers une autre vue ou effectuer d'autres actions
            return redirect('gestion-depots')
    else:
        editAdressForm = AdresseEditForm(instance=adresse)
        depot_edit_formset = depotEditFormSet(instance=depot)

    return render(request, 'edition_depot.html', {'depot_edit_formset': depot_edit_formset, 'editAdressForm': editAdressForm, 'depot': depot})
"""

# CORRECTION : VERSION DU CODE 1 :
"""
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

"""


# Formulaire d'édition d'un article :
def edition_article(request, no_article):
    article = get_object_or_404(Article, pk=no_article)

    if request.method == 'POST':
        form = ArticleEditForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # Rediriger vers une autre vue ou effectuer d'autres actions
            return redirect('gestion-stock')
    else:
        form = ArticleEditForm(instance=article)

    return render(request, 'edition_article.html', {'form': form, 'depot': article})




# Formulaire d'édition d'un rayon :
def edition_rayon(request, no_rayon):
    rayon = get_object_or_404(Rayon, pk=no_rayon)

    if request.method == 'POST':
        form = RayonEditForm(request.POST, instance=rayon)
        if form.is_valid():
            form.save()
            # Rediriger vers une autre vue ou effectuer d'autres actions
            return redirect('gestion-rayons')
    else:
        form = RayonEditForm(instance=rayon)

    return render(request, 'edition_rayon.html', {'form': form, 'rayon': rayon})








