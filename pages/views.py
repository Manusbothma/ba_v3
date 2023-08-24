from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)


from .models import Profile, Service
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(ListView):
    model = Profile
    template_name = "pages/about.html"


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"


class ServicesPageView(ListView):
    model = Service
    template_name = "pages/services.html"


class CreateService(CreateView):
    model = Service
    fields = ["service_title", "description", "image"]
    template_name = "pages/create_service.html"
    success_url = reverse_lazy("services")


class ServiceDetail(DetailView):
    model = Service
    fields = ["service_title", "description", "image"]
    template_name = "pages/service_detail.html"


class UpdateService(UpdateView):
    template_name = "pages/update_service.html"
    model = Service
    fields = ["service_title", "description", "image"]
    success_url = reverse_lazy("services")
