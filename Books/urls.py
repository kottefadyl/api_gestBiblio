from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("livre", views.LivreViewSet)
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
    path("refresh1",views.InsertWithFile, name="refresh1"),
    path("refresh2",views.InsertToFile, name="refresh2"),
    path("stripe",views.create_payment_intent, name="stripe"),
    path("book_per_catalogue/<str:catalogue>",views.book_per_catalogue, name="book_per_catalogue"),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]