from django.shortcuts import render
from django.utils import timezone
from .models import Pedido, Articulo
from .forms import PostForm, PostFormArticulos
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
import csv
from rest_framework import viewsets
from .serializers import CustomerSerializer, ArticleSerializer
import os


class CustomerViewSet(viewsets.ModelViewSet):
    model = Pedido
    queryset = Pedido.objects.all()
    serializer_class = CustomerSerializer

class ArticlesViewSet(viewsets.ModelViewSet):
    model = Articulo
    queryset = Articulo.objects.all()
    serializer_class = ArticleSerializer

def lista_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'pedidos.html', {'pedidos': pedidos})

def articulos_nuevos(request, pk):
    pedido_obtenido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PostFormArticulos(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pedido = pedido_obtenido
            post.save()
            return redirect('articulos_new', pk = pk)
    else:
        form = PostFormArticulos()
    return render(request, 'post_articulo.html', {'form': form})

def pedido_nuevo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect('articulos_new', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_pedido.html', {'form': form})

def pedido_detalle(request, pk):
    objeto1 = Pedido.objects.get(pk=pk)
    objeto2 = Articulo.objects.filter(pedido = objeto1)

    return render(request, "pedido_detail.html", {'pedido': objeto1, 'articulos': objeto2})

def envia_mail(request, pk):
    objeto1 = Pedido.objects.get(pk=pk)
    objeto2 = Articulo.objects.filter(pedido=objeto1)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pedido.csv"'
    with open('pedido.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        columnas = []
        writer.writerows([['Usuario','GLN','Precio']])
        for p in objeto2:
            columnas = [objeto1.usuario.pk,p.GLN,p.precio]
            writer.writerows([columnas])
        # writer.save(response)
        f.close()
        email = EmailMessage(
            'Pedidos usuario: ' + str(objeto1.usuario.username),
            '',
            'hecgarco@gmail.com',
            ['hecgarco@gmail.com'],
            [''],
            reply_to=[''],
            headers={'Message-ID': 'foo'},
        )
        email.attach_file('pedido.csv')
        email.send(fail_silently=False)

        #os.remove('pedido.csv')
    return render(request, "pedido_detail.html", {'pedido': objeto1, 'articulos': objeto2})
