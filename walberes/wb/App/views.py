from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import UserForm
from django.urls import reverse_lazy

class MainView(TemplateView):
    template_name = "main.html"

class CreateUser(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("main")
    template_name = 'reg.html'