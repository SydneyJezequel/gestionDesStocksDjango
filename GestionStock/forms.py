# Dépendances :
from django import forms
from django.forms import inlineformset_factory
from GestionStock.models import Article, Depot, Adresse, Rayon









# ************************************* Formulaires d'ajout ************************************* #




# Formulaire : Ajouter un article en stock :
class addArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nom_article', 'quantite', 'genre', 'no_rayon']




# Formulaire : Ajouter un dépôt :
class addDepotForm(forms.ModelForm):
    class Meta:
        model = Depot
        fields = ['nom_depot']




# Formulaire : Ajouter un dépôt avec une adresse :
class addAdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['no_de_rue', 'rue', 'code_postal', 'ville']




#  Formulaire qui combine Un dépôt + Son Adresse :
addDepotFormSet = inlineformset_factory(Adresse, Depot, form=addDepotForm, fields=['nom_depot'], extra=1)




class addRayonForm(forms.ModelForm):
    class Meta:
        model = Rayon
        fields = ['nombre_de_cellule', 'no_depot']









# ************************************* Formulaires d'édition ************************************* #




# Formulaire d'Edition d'un Dépot :
class DepotEditForm(forms.ModelForm):
    class Meta:
        model = Depot
        fields = ['nom_depot', 'no_adresse']




# Formulaire d'Edition d'un Article :
class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nom_article', 'quantite', 'genre', 'no_rayon']




# Formulaire d'Edition d'un Dépot :
class RayonEditForm(forms.ModelForm):
    class Meta:
        model = Rayon
        fields = ['nombre_de_cellule', 'no_depot']




# Formulaire d'Edition d'un Dépot :
class AdresseEditForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['no_de_rue', 'rue', 'code_postal', 'ville']




#  Formulaire d'Edition qui combine Un dépôt + Son Adresse :
depotEditFormSet = inlineformset_factory(Adresse, Depot, form=DepotEditForm, fields=['nom_depot'], extra=1)

