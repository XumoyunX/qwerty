from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import MainIndex, Mahsulot, Searchq, Korzinka, AddCart

app_name = "main"

urlpatterns = [
    path("", MainIndex.as_view(), name="index"),
    path("korzinka/", Korzinka.as_view(), name="korzinka"),
    path("mahsulot/<int:id>/", Mahsulot.as_view(), name="mahsulot"),
    path("searchq/", Searchq.as_view(), name="searchq"),
    path("add-cart/<int:pk>/", AddCart.as_view(), name="add-cart"),
]
