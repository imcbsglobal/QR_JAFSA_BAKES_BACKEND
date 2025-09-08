from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save-person/', views.save_person, name='save_person'),
    path('persons/', views.get_all_persons, name='get_all_persons'),
]

