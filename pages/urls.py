from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.PagesView.as_view(), name="home"),
    path("finans/", views.FinansPagesView.as_view(), name="finans"),
    path("tecnoblog/", views.TecblogPagesView.as_view(), name="tecnoblog"),
    path(
        "noticias/",
        views.NoticiasCidadePagesView.as_view(),
        name="noticiascidade",
    ),
    path(
        "noticias/brasil/",
        views.NoticiasCidadeBrasil.as_view(),
        name="noticiasbrasil",
    ),
    path(
        "noticias/fotos/",
        views.NoticiasCidadeFotos.as_view(),
        name="noticiasfotos",
    ),
    path(
        "noticias/nova-legislacao/",
        views.NoticiasCidadeNovaLegislacao.as_view(),
        name="noticiasnova-legislacao",
    ),
    path("chalehotel/", views.ChalePagesView.as_view(), name="chalehotel"),
    path(
        "museuinternacio/",
        views.MuseuPagesView.as_view(),
        name="museuinternacional",
    ),
    path(
        "clonespotify/",
        views.SpotifyPagesView.as_view(),
        name="clonespotify",
    ),
]
