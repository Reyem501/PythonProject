from django.forms.models import ModelForm
from .models import Enseignant, Materiel


class EnseignantForm(ModelForm):
    class Meta:
        model = Enseignant

        fields = (
            "nom",
            "prenom",
        )


class MaterielForm(ModelForm):
    class Meta:
        model = Materiel

        fields = (
            "libelle_materiel",
            "responsable",
            "enseignant",
            "salle",
        )
