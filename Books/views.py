import pandas as pd
from django.shortcuts import render
from django.http import request
from .models import Book,Auteur,Catalogue,MaisonEdition,Louer,Client,Concerner,Commande,Abonnement,Effectuer,Abonne
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'titre', 'libele','prix','quantite','image')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'nom', 'prenom','tel')

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ('id', 'date')

class ConcernerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concerner
        fields = ('id', 'quantite', 'montant')


class AbonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonne
        fields = ('id', 'nom', 'prenom','email','tel','mdp','img','dateInsert')

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = ('id', 'nom', 'prenom','dateNaiss')

class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = ('id', 'intitule', 'nbrBook')

class MaisonEditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaisonEdition
        fields = ('id', 'intitule')

class LouerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Louer
        fields = ('id', 'idbook', 'idabonne','duree')

class EffectuerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effectuer
        fields = ('id', 'idabonne', 'idabonnement')

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = ('id', 'intitule', 'description','duree','nombreLivre')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().values()
    serializer_class = ClientSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all().values()
    serializer_class = CommandeSerializer

class ConcernerViewSet(viewsets.ModelViewSet):
    queryset = Concerner.objects.all().values()
    serializer_class = ConcernerSerializer

class AbonnementViewSet(viewsets.ModelViewSet):
    queryset = Abonnement.objects.all().values()
    serializer_class = AbonnementSerializer

class AbonneViewSet(viewsets.ModelViewSet):
    queryset = Abonne.objects.all()
    serializer_class = AbonneSerializer
    
    def perform_create(self, serializer):
        username = serializer.validated_data['nom']
        password = serializer.validated_data['mdp']
        email = serializer.validated_data['email']
        user = User.objects.create_user(username=username,password=password, email=email)
        abonne = serializer.save(user=user)
        return Response(serializer.data)
   
class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    
class CatalogueViewSet(viewsets.ModelViewSet):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer
    
class MaisonEditionViewSet(viewsets.ModelViewSet):
    queryset = MaisonEdition.objects.all()
    serializer_class = MaisonEditionSerializer
    
class LouerViewSet(viewsets.ModelViewSet):
    queryset = Louer.objects.all()
    serializer_class = LouerSerializer
    
class EffectuerViewSet(viewsets.ModelViewSet):
    queryset = Effectuer.objects.all()
    serializer_class = EffectuerSerializer
  

def createWithFile(self, request, *args, **kwargs):
    Book.objects.all().delete()
    df = pd.read_excel('db.xlsx')
    data_dicts = df.to_dict(orient='records') 
    data = []
    for item in data_dicts:
        data.append(item)
    Book.objects.save_many(data)
    print("success")
    
        
    


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response(status=204)
        
        
class LoginView(APIView):

    def post(self, request):
        username = request.data.get('nom')
        password = request.data.get('mdp')

        user = authenticate(username=username, password=password)

        if user is not None:
            token = Token.objects.create(user=user)
            return Response({'token': token.key})
        else:
            return Response(status=401)

    
    
