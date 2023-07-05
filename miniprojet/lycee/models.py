from django.db import models


# Create your models here.

class Enseignant(models.Model):
    first_name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        verbose_name="lastname",
        help_text="last name of the enseignant",
        blank=False,  # pas de champ vide
        null=False,  # pas de champ null (a conjuguer avec default
        default="???",
        max_length=255,  # taille maximale du champ
    )
    cursus = models.ForeignKey(
        Cursus,
        on_delete=models.CASCADE,  # necessaire selon la version de Django
        null=True
    )

    def __str__(self):
        return self.last_name


class Materiel(models.Model):
    libelle_materiel = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    quantite_materiel = models.IntegerField(blank=False, null=False)  # Ajout du champ "quantite"

    def __str__(self):
        return self.last_name