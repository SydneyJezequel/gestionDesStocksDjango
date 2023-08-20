# Dépendances :
from django.db import models








# ************************************* Liste des classes ************************************* #




# Classe Adresse :
class Adresse(models.Model):
    no_adresse = models.AutoField(primary_key=True)
    no_de_rue = models.CharField(max_length=50)
    rue = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=20)
    ville = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.no_adresse}: {self.no_de_rue}, {self.rue}, {self.code_postal}, {self.ville}"




# Classe Dépôt :
class Depot(models.Model):
    no_depot = models.AutoField(primary_key=True)
    nom_depot = models.CharField(max_length=100)
    no_adresse = models.OneToOneField(Adresse, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.no_depot}: {self.nom_depot}"




# Classe Rayon :
class Rayon(models.Model):
    no_rayon = models.AutoField(primary_key=True)
    nombre_de_cellule = models.IntegerField()
    no_depot = models.ForeignKey(Depot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.no_rayon}: Rayon in {self.no_depot}"




# Classe Article :
class Article(models.Model):

    # Classe imbriquée :
    class Type(models.TextChoices):
        Alimentaire = 'ALIM'
        Menage = 'MEN'
        Electromenager = 'ELEC'

    # Attributs de la classe Article :
    no_article = models.AutoField(primary_key=True)
    nom_article = models.CharField(max_length=100)
    quantite = models.IntegerField()
    genre = models.fields.CharField(choices=Type.choices, max_length=5)
    no_rayon = models.ManyToManyField(Rayon)

    def __str__(self):
        return f"{self.nom_article}"






