from django.views.generic import TemplateView


class PagesView(TemplateView):
    template_name = "pages/index.html"


class ChalePagesView(TemplateView):
    template_name = "pages/chalehotel/index.html"


class FinansPagesView(TemplateView):
    template_name = "pages/finans/index.html"


class TecblogPagesView(TemplateView):
    template_name = "pages/tecblog/index.html"


class NoticiasCidadePagesView(TemplateView):
    template_name = "pages/noticiascidade/index.html"


class NoticiasCidadeBrasil(TemplateView):
    template_name = "pages/noticiascidade/brasil.html"


class NoticiasCidadeFotos(TemplateView):
    template_name = "pages/noticiascidade/fotos.html"


class NoticiasCidadeNovaLegislacao(TemplateView):
    template_name = "pages/noticiascidade/mova-legislacao.html"


class MuseuPagesView(TemplateView):
    template_name = "pages/museuinternacional/index.html"


class SpotifyPagesView(TemplateView):
    template_name = "pages/spotify/index.html"
