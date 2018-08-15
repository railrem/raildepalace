from django.urls import path
from . import views
urlpatterns = [
    path('api/beer/', views.BeerListCreate.as_view()),
]