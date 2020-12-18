from django.shortcuts import render
from django.contrib.auth.view import LoginView
# Create your views here.

class LoginFormView(LoginView):
    template_name = 'templates/index.html'

