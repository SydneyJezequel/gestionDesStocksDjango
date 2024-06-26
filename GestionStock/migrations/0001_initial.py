# Generated by Django 4.2.4 on 2023-08-14 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('no_adresse', models.AutoField(primary_key=True, serialize=False)),
                ('no_de_rue', models.CharField(max_length=50)),
                ('rue', models.CharField(max_length=100)),
                ('code_postal', models.CharField(max_length=20)),
                ('ville', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('no_depot', models.AutoField(primary_key=True, serialize=False)),
                ('nom_depot', models.CharField(max_length=100)),
                ('no_adresse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GestionStock.adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Rayon',
            fields=[
                ('no_rayon', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_de_cellule', models.IntegerField()),
                ('no_depot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionStock.depot')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('no_article', models.AutoField(primary_key=True, serialize=False)),
                ('nom_article', models.CharField(max_length=100)),
                ('quantite', models.IntegerField()),
                ('no_rayon', models.ManyToManyField(to='GestionStock.rayon')),
            ],
        ),
    ]
