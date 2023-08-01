from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('medie/', MediaValView.as_view(), name='medie'),
    path('add/', AddPersonView.as_view(), name = 'add'),
path('update/<int:pk>', PersonUpdateView.as_view(), name = 'update'),
path('delete/<int:pk>', PersonDeleteView.as_view(), name = 'delete'),
path('add_servant/', AddServantView.as_view(), name = 'add_servant'),
path('update_servant/<int:pk>', ServantUpdateView.as_view(), name = 'update_servant'),
path('delete_servant/<int:pk>', ServantDeleteView.as_view(), name = 'delete_servant'),
]