from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/<str:name>', views.about, name='about'),
    path('spells', views.spell, name='spells'),
]
