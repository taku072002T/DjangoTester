from django.urls import path

from .views import IndexView
from .views import ErrorView

urlpatterns = [
    path('',IndexView.as_view()),
    path('error',ErrorView.as_view())
    
]