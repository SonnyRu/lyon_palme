from django.db import models
from django.contrib.auth.models import User
from encrypted_model_fields.fields import EncryptedCharField
# Create your models here.
class ENTRAINEUR(models.Model):
    """
    Stock les entraineurs de la base de donnée, relation avec le model :model:`auth.User`
    """
    Nom = EncryptedCharField(max_length=20, null=False)
    Prenom = EncryptedCharField(max_length=20, null=False)
    Email = models.EmailField(max_length=254, null=False)
    Tel = models.CharField(max_length=20, null=False, default='0699999999')
    DateCreation = models.DateTimeField(auto_now_add=True, null=False)
    ListeRoles = (
        ('Entraineur', 'Entraineur'),
        ('Entraineur Resp. Planning', 'Entraineur Resp. Planning')
    )
    Identifiant = models.CharField(max_length=20, null=False)
    Role = models.CharField(max_length=50, null=False, default='Entraineur', choices=ListeRoles)
    UserId = models.ForeignKey(User, related_name='UserId', on_delete=models.CASCADE)
    class Meta:
        """
        Ordoné par date de création
        """
        ordering = ['-DateCreation']
    def __str__(self):
        """
        Retourne le nom et le prénom de son propre model
        """
        return self.Nom + ' ' + self.Prenom
class ENTRAINEMENT(models.Model):
    """
    Stock les entrainements de la base de donnée
    """
    Titre = models.CharField(max_length=30, null=False)
    DateEntrainement = models.DateField(null=False)
    NomPartie1 = models.CharField(max_length=30, null=False)
    Partie1 = models.TextField(max_length=254, null=False)
    TempsPartie1 = models.TimeField(null=False)
    DistancePartie1 = models.CharField(max_length=20, null=False)
    NomPartie2 = models.CharField(max_length=30, null=False)
    Partie2 = models.TextField(max_length=254, null=False)
    TempsPartie2 = models.TimeField(null=False)
    DistancePartie2 = models.CharField(max_length=20, null=False)
    NomPartie3 = models.CharField(max_length=30, null=False)
    Partie3 = models.TextField(max_length=254, null=False)
    TempsPartie3 = models.TimeField(null=False)
    DistancePartie3 = models.CharField(max_length=20, null=False)
    DateCreation = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        """
        Ordoné par date de création
        """
        ordering = ['-DateCreation']
    def __str__(self):
        """
        Retourne le titre de son propre model
        """
        return self.Titre
class ATTRIBUER(models.Model):
    """
    Stock les attributions des entrainements aux entraineurs, relatif avec les modèles
    :model:`palmplanning.ENTRAINEUR` et :model:`palmplanning.ENTRAINEMENT`
    """
    EntraineurAttribuer = models.ForeignKey(ENTRAINEUR, related_name="EntraineurAttribuer", on_delete=models.CASCADE)
    EntrainementAttribuer = models.ForeignKey(ENTRAINEMENT, related_name="EntrainementAttribuer", on_delete=models.CASCADE)
    DateAttribution = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        """
        Ordoné par date de création
        """
        ordering = ['-DateAttribution']
    def __str__(self):
        """
        Retourne l'identifiant de l'utilisateur relatif au model :model:`palmplanning.ENTRAINEUR`
        Ainsi que le titre de l'entrainement aossicé au model :model:`palmplanning.ENTRAINEMENT`
        """
        return self.EntraineurAttribuer.Identifiant + ' | ' + self.EntrainementAttribuer.Titre
class COMMENTAIRE(models.Model):
    """
    Stock les commentaires des entraineurs relatif à leur entrainement, relation avec les modèles
    :model:`palmplanning.ENTRAINEUR` et :model:`palmplanning.ENTRAINEMENT`
    """
    UserCommentaire = models.ForeignKey(ENTRAINEUR, related_name="UserCommentaire", on_delete=models.CASCADE)
    EntrainementCommentaire = models.ForeignKey(ENTRAINEMENT, related_name="EntrainementCommentaire", on_delete=models.CASCADE)
    Commentaire = models.TextField(max_length=254, null=False)
    DateCommentaire = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        """
        Ordoné par date de création
        """
        ordering = ['-DateCommentaire']
    def __str__(self):
        """
        Retourne le nom d'utilisateur relatif au model :model:`auth.User`
        Ainsi que le titre de l'entrainement associé au model :model:`palmplanning.ENTRAINEMENT`
        """
        return self.UserCommentaire.Identifiant + ' | ' + self.EntrainementCommentaire.Titre