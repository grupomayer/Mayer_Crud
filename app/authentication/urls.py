from django.urls import path
from .views import  AuthenticationView


urlpatterns = [
    path('authentication/', AuthenticationView.as_view()),

]
