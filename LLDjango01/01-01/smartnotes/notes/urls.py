from django.urls import path

from . import views

urlpatterns = [
    path("notes", views.NotesListView.as_view(), name="notes"),
    path("note/<int:pk>", views.NotesDetailView.as_view(), name="note"),
    path("note/new", views.NotesCreateView.as_view(), name="note.new"),
    path("note/<int:pk>/edit", views.NotesUpdateView.as_view(), name="note.update"),
    path("note/<int:pk>/delete", views.NotesDeleteView.as_view(), name="note.delete"),
]
