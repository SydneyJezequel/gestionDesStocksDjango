# Formulaires :
from django import forms
from GestionStock.models import Article, Depot




# Formulaire : Ajouter un article en stock :
class addArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nom_article', 'quantite', 'genre', 'no_rayon']




# Formulaire : Ajouter un dépôt :
class addDepotForm(forms.ModelForm):
    class Meta:
        model = Depot
        fields = ['nom_depot', 'no_adresse']



