# Formulaires :

from django import forms
from GestionStock.models import Article


# Formulaire : Ajouter un article en stock :
class addArticleForm(forms.Form):
    class Meta:
        model = Article
        fields = ['nom_article', 'quantite', 'genre', 'no_rayon']

    def save(self):
        pass