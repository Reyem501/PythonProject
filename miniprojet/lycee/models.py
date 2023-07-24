from django.db import models


# Create your models here.

class Emprunt(models.Model):
    budget = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    def __str__(self):
        return self.budget


class Enseignant(models.Model):
    prenom = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    nom = models.CharField(
        verbose_name="lastname",
        help_text="last name of the enseignant",
        blank=False,  # pas de champ vide
        null=False,  # pas de champ null (a conjuguer avec default
        default="???",
        max_length=50,  # taille maximale du champ
    )
    def __str__(self):
        return self.nom


class Materiel(models.Model):
    libelle_materiel = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    localisation = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    responsable = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    enseignant = models.ForeignKey(
        Enseignant,
        on_delete=models.CASCADE,  # necessaire selon la version de Django
        null=True
    )
    def __str__(self):
        return self.libelle_materiel

class Passation(models.Model):
    date_pass = models.DateField(
        verbose_name='date de passation',
        blank=False,
        null=False
    )
    lieu_pass = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    occasion_pass = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    objectif_pos2 = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    materiel = models.ForeignKey(
        Materiel,
        on_delete=models.CASCADE,  # necessaire selon la version de Django
        null=True
    )
    def __str__(self):
        return self.libelle_acc


class Accessoire(models.Model):
    libelle_acc = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    etat_acc = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    materiel = models.ForeignKey(
        Materiel,
        on_delete=models.CASCADE,  # necessaire selon la version de Django
        null=True
    )
    def __str__(self):
        return self.libelle_acc