from django.shortcuts import render
from django.utils import timezone
from .models import Pedido, Articulo
from .forms import PostForm, PostFormArticulos
from django.shortcuts import redirect, get_object_or_404

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
