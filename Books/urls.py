from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("books", views.BookViewSet)
router.register("client", views.ClientViewSet)
router.register("commande", views.CommandeViewSet)
router.register("concerner", views.ConcernerViewSet)
router.register("abonnement", views.AbonnementViewSet)
router.register("abonne", views.AbonneViewSet)
router.register("MaisonEdition", views.MaisonEditionViewSet)
router.register("Catalogue", views.CatalogueViewSet)
router.register("Louer", views.LouerViewSet)
router.register("Effectuer", views.EffectuerViewSet)
router.register("auteur", views.AuteurViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("refresh",views.createWithFile, name="refresh"),
    path('api/login/', views.LoginView.as_view()),
    path('api/logout/', views.LogoutView.as_view()),
]