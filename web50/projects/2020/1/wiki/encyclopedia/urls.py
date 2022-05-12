from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random", views.pickRandom, name = "random"),
    path("wiki/<str:id>", views.entryInfo, name = "entryInfo"),
    path("addNewPage", views.addNewPage, name = "addNewPage"),
    path("search", views.searchEntry, name = "searchEntry"),
    path("wiki/<str:id>/edit", views.editPage, name = "edit"),
]
