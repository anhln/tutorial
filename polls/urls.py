
from django.urls import path, include
from polls.views import IndexView, AuthorizedView, LoginInterfaceView, LogoutInterfaceView, SignupView

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('authorize', AuthorizedView.as_view()),
    path('login', LoginInterfaceView.as_view(), name='login'),
    path('logout', LogoutInterfaceView.as_view(), name = 'logout'),
    path('signup', SignupView.as_view(), name = 'signup'),
]
