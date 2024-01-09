from django.contrib import admin
from .models import Livre,Auteur,Catalogue,MaisonEdition,Louer,Client,Concerner,Commande,Abonnement,Effectuer,Abonne

admin.site.register(Abonne)
admin.site.register(Abonnement)
admin.site.register(Effectuer)
admin.site.register(Client)
admin.site.register(Concerner)
admin.site.register(Commande)
admin.site.register(Livre)
admin.site.register(Auteur)
admin.site.register(Catalogue)
admin.site.register(MaisonEdition)
admin.site.register(Louer)