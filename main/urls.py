
from django.contrib import admin
from django.urls import path, include
from FINECAP.views import IndexView, ReservaListView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView, detalhar_reserva, StandListView, StandCreateView, StandUpdateView, StandDeleteView

from django.views import generic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('reserva/',ReservaCreateView.as_view(),name='criar_reserva'),
    path('reserva/listar',ReservaListView.as_view(),name='reservas-list'),
    path('reserva/editar/<int:pk>/', ReservaUpdateView.as_view(), name='reservas-update'),
    path('reserva/delete/<int:pk>/', ReservaDeleteView.as_view(), name='reservas-delete'), #_____________________________#
    path('reserva/detalhar',detalhar_reserva,name='detalhar_reserva'),
    path('stand/',StandCreateView.as_view(),name='criar_stand'),
    path('stand/listar',StandListView.as_view(),name='stands-list'),
    path('stand/editar/<int:pk>/', StandUpdateView.as_view(), name='stands-update'),
    path('stand/delete/<int:pk>/', StandDeleteView.as_view(), name='stands-delete'),

    
]
