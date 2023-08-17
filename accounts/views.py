from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class SignUpPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy
    template_name = "registration/signup.html"