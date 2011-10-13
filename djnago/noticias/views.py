# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Noticia
from django.shortcuts import get_object_or_404

def index(request):
    noticia = Noticia.objects.all()[:4]

    news1 = noticia[0]
    news2 = noticia[1]
    news3 = noticia[2]
    news4 = noticia[3]
    
    return render_to_response("index.html", {'noticia1': news1, 'noticia2': news2, 'noticia3': news3, 'noticia4': news4})

def noticia(request, url):

    
    noticia_objeto = get_object_or_404(Noticia, url=url)
    
    
    return render_to_response("noticia.html", {'noticia': noticia_objeto})
