
from django.urls import path
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('notes', NoteListView.as_view(), name="note.list"),
    path('notes/<int:pk>', NoteDetailView.as_view(), name="note.detail"),
    path('notes/<int:pk>/edit', NoteUpdateView.as_view(), name="note.update"),
    path('notes/<int:pk>/delete', NoteDeleteView.as_view(), name="note.delete"),
    path('notes/new', NoteCreateView.as_view(), name="note.new"),
]
