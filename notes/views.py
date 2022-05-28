from django.shortcuts import render
from django.http import Http404
from .models import Note
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .forms import NoteForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect


# Create your views here.
class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/smarts/notes'
    template_name = 'notes/note_delete.html'
    
    
class NoteUpdateView(UpdateView):
    model = Note
    success_url = '/smarts/notes'
    form_class = NoteForm
    

class NoteCreateView(CreateView):
    model = Note
    success_url = '/smarts/notes'
    form_class = NoteForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.success_url)
    
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/note_list.html"
    login_url = '/login'
    
    def get_queryset(self):
        return self.request.user.note_user.all()
        
        
class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/note_detail.html"
