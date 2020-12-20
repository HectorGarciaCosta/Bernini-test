"""Bernini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from login.views import LoginFormView
from pedido.views import lista_pedidos, pedido_nuevo, articulos_nuevos, pedido_detalle, envia_mail
from rest_framework.routers import DefaultRouter
from pedido.views import CustomerViewSet, ArticlesViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginFormView.as_view()),
    path('accounts/profile/', lista_pedidos, name='lista_pedidos'),
    path('post/new', pedido_nuevo, name='post_new'),
    path('post/<int:pk>/', articulos_nuevos, name='articulos_new'),
    path('post/<int:pk>/detalle/', pedido_detalle, name='pedido_detalle'),
    path('post/<int:pk>/detalle/envia_mail', envia_mail, name='envia_mail'),
]
router = DefaultRouter()
router.register('pedidos', CustomerViewSet, 'pedidos')
router.register('articulos', ArticlesViewSet, 'articulos')
urlpatterns += router.urls