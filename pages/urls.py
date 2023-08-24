from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ServicesPageView,
    ServiceCreate,
    ServiceDetail,
    ServiceUpdate,
    ServiceDelete,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("services/", ServicesPageView.as_view(), name="services"),
    path("service_create/", ServiceCreate.as_view(), name="service_create"),
    path("service/detail/<int:pk>/", ServiceDetail.as_view(), name="service_detail"),
    path("service/update/<int:pk>/", ServiceUpdate.as_view(), name="service_update"),
    path("service/delete/<int:pk>/", ServiceDelete.as_view(), name="service_delete"),
]
