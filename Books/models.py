from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    idauteur = models.ForeignKey(to="Auteur", on_delete=models.CASCADE)
    idcatalogue = models.ForeignKey(to="Catalogue", on_delete=models.CASCADE)
    idmaisonEdition = models.ForeignKey(to="MaisonEdition", on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    libele = models.CharField(max_length=255)
    prix = models.IntegerField()
    quantite = models.IntegerField()
    image = models.ImageField(upload_to='images')    
    
    def __str__(self):
        return self.titre

class Abonne(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel = models.IntegerField()
    mdp = models.CharField(max_length=255)
    img = models.ImageField(upload_to="image")
    dateInsert = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel = models.IntegerField()
    
    
    def __str__(self):
        return self.nom

class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    Date = models.DateTimeField(auto_now=True)
    nomcli = models.CharField(max_length=255)
    prenomcli = models.CharField(max_length=255)
    emailcli = models.EmailField(max_length=255)
    telcli = models.IntegerField()
    
    def __str__(self):
        return self.id

class Concerner(models.Model):
    id = models.AutoField(primary_key=True)
    quantite = models.IntegerField()
    montant = models.IntegerField()

    def __str__(self):
        return self.id

class Abonnement(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    dateDeb = models.DateField()
    dateFin = models.DateField()
    nombreLivre = models.IntegerField()
        
    def __str__(self):
        return self.intitule


class Effectuer(models.Model):
    id = models.AutoField(primary_key=True)
    idabonne = models.ForeignKey(to="Abonne",on_delete=models.CASCADE)
    idabonnement = models.ForeignKey(to="Abonnement",on_delete=models.CASCADE)
    def __str__(self):
        return self.id


class Auteur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    dateNaiss = models.DateField(max_length=255)
    
    def __str__(self):
        return self.nom

class MaisonEdition(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=255)
     
    def __str__(self):
        return self.intitule

class Catalogue(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=255)
    nbrBook = models.IntegerField()
    def __str__(self):
        return self.intitule


class Louer(models.Model):
    id = models.AutoField(primary_key=True)
    idbook = models.ForeignKey(to="Book",on_delete=models.CASCADE)
    idabonne = models.ForeignKey(to="Abonne",on_delete=models.CASCADE)
    duree = models.IntegerField()
    def __str__(self):
        return self.ref
