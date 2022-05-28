
from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = 'smarts/notes'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('note.list')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = 'login.html'
    
    
class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'
        

class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {"date": datetime.now()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'authorized.html'
    extra_context = {"date": datetime.now()}
    login_url = 'admin/'
    
