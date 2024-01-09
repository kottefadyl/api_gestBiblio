import pandas as pd
from .models import Livre,Auteur,Catalogue,MaisonEdition,Louer,Client,Concerner,Commande,Abonnement,Effectuer,Abonne
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Transaction
from django.contrib.auth import logout,authenticate


class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ('id','idauteur','idcatalogue','idmaisonEdition', 'titre', 'libele','description','prix','quantite','image')

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
        fields = ('id', 'intitule', 'nbrBook','image')

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
        fields = ('id', 'intitule', 'description','duree','nombreLivre','montant')

  
class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

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
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    


class AbonneViewSet(viewsets.ModelViewSet):
    queryset = Abonne.objects.all()
    serializer_class = AbonneSerializer
    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            donnee = AbonneSerializer(data=request.POST)
            if donnee.is_valid():
                abonne = Abonne.objects.create(nom = donnee.data['nom'],prenom = donnee.data['prenom'],email = donnee.data['email'],
                                           tel = donnee.data['tel'],mdp = donnee.data['mdp'],img = donnee.data['img'])     
                User.objects.create_user(username=donnee.data['nom']+donnee.data['prenom'],password=donnee.data['mdp'],
                                     email=donnee.data['email'])
                print(donnee.data) 
            print(donnee.data)
            return Response({'success'})

        return Response({'error occured'})

   
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
  
@api_view(['GET'])
def InsertWithFile(request,*args, **kwargs):
    Abonne.objects.all().delete()
    Abonnement.objects.all().delete()
    Auteur.objects.all().delete()
    Livre.objects.all().delete()
    Catalogue.objects.all().delete()
    Commande.objects.all().delete()
    MaisonEdition.objects.all().delete()
    Client.objects.all().delete()
    df1 = pd.read_excel('db.xlsx',sheet_name='Abonnes')
    df2 = pd.read_excel('db.xlsx',sheet_name='Abonnement')
    df3 = pd.read_excel('db.xlsx',sheet_name='Auteurs')
    df4 = pd.read_excel('db.xlsx',sheet_name='Livres')
    df5 = pd.read_excel('db.xlsx',sheet_name='Catalogues')
    df6 = pd.read_excel('db.xlsx',sheet_name='Commandes')
    df7 = pd.read_excel('db.xlsx',sheet_name='Maisons Editions')
    df8 = pd.read_excel('db.xlsx',sheet_name='Clients')
    data_dicts1 = df1.to_dict(orient='records') 
    data_dicts2 = df2.to_dict(orient='records') 
    data_dicts3 = df3.to_dict(orient='records') 
    data_dicts4 = df4.to_dict(orient='records') 
    data_dicts5 = df5.to_dict(orient='records') 
    data_dicts6 = df6.to_dict(orient='records') 
    data_dicts7 = df7.to_dict(orient='records') 
    data_dicts8 = df8.to_dict(orient='records') 
    for item in data_dicts1:
        Abonne.objects.create(nom=item['nom'],prenom=item['prenom'],email=item['email'],tel=item['tel'])
    
    for item in data_dicts2:
        Abonnement.objects.create(intitule=item['intitule'],description=item['description'],duree=item['duree'],nombreLivre=item['nombreLivre'],montant=item['montant'])
    
    for item in data_dicts3:
        Auteur.objects.create(nom=item['nom'],prenom=item['prenom'],dateNaiss=item['dateNaiss'])
    
    for item in data_dicts4:
        Livre.objects.create(idauteur=item['idauteur'],idcatalogue=item['idcatalogue'],idmaisonEdition=item['idmaisonEdition'],
                            titre=item['titre'],libele=item['libele'],description=item['description'],prix=item['prix'],
                            quantite=item['quantite'])
    
    for item in data_dicts5:
        Catalogue.objects.create(intitule=item['nom'],nbrbook=item['prenom'])
    
    for item in data_dicts6:
        Commande.objects.create(nomcli=item['nomcli'],prenomcli=item['prenomcli'],emailcli=item['emailcli'],telcli=item['telcli'],Date=item['Date'])
    
    for item in data_dicts7:
        MaisonEdition.objects.create(intitule=item['intitule'])
    
    for item in data_dicts8:
        Client.objects.create(nom=item['nom'],prenom=item['prenom'],email=item['email'],tel=item['tel'])
    
    return Response({"success to files into db"})

@api_view(['GET'])
def InsertToFile(request,*args, **kwargs):
    queryset2 = Abonne.objects.all()
    queryset1 = Livre.objects.all()
    queryset3 = Abonnement.objects.all()
    queryset4 = Auteur.objects.all()
    queryset5 = Catalogue.objects.all()
    queryset6 = MaisonEdition.objects.all()
    queryset7 = Commande.objects.all()
    queryset8 = Client.objects.all()
    df1 = pd.DataFrame(queryset1.values())
    df2 = pd.DataFrame(queryset2.values())
    df3 = pd.DataFrame(queryset3.values())
    df4 = pd.DataFrame(queryset4.values())
    df5 = pd.DataFrame(queryset5.values())
    df6 = pd.DataFrame(queryset6.values())
    df7 = pd.DataFrame(queryset7.values())
    df8 = pd.DataFrame(queryset8.values())
    df1.to_excel('db.xlsx',sheet_name='Livres',index=False)
    df2.to_excel('db.xlsx',sheet_name='Abonnes',index=False)
    df3.to_excel('db.xlsx',sheet_name='Abonnements',index=False)
    df4.to_excel('db.xlsx',sheet_name='Auteurs',index=False)
    df5.to_excel('db.xlsx',sheet_name='Catalogues',index=False)
    df6.to_excel('db.xlsx',sheet_name='Maison Edition',index=False)
    df7.to_excel('db.xlsx',sheet_name='Commande',index=False)
    df8.to_excel('db.xlsx',sheet_name='Client',index=False)
    return Response({"success to db into file"})
      
      
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

@api_view(['GET','POST'])
def book_per_catalogue(request, catalogue):
    try:
        catalog = Catalogue.objects.get(intitule=catalogue)
        livre = Livre.objects.filter(idcatalogue=catalog).values()
    except Catalogue.DoesNotExist:
        livre=[]
        catalog=None
    return Response({"livres par catalogue": livre})

stripe.api_key = 'votre_cle_secrete_stripe'
@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        try:
            # Obtenez les données du paiement depuis le frontend
            data = json.loads(request.body)
            amount = data['amount']

            # Créez une intention de paiement avec Stripe
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',  # Changez selon votre devise
            )

            return JsonResponse({'clientSecret': payment_intent.client_secret})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)