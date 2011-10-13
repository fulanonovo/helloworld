from django.contrib.syndication.feeds import Feed

from models import Noticia

class UltimasNoticias(Feed):
    title = 'Ultimas noticias do blog do Alatazan'
    link = '/'

    def items(self):
        return Noticia.objects.all()

    def item_link(self, noticia):
        return '/noticia/%d/'%noticia.id
