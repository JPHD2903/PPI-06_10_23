from django.shortcuts import render,get_object_or_404,redirect
from .models import Reserva, Stand
from .form import ReservaForm, StandForm
from django.views import View
from django.views.generic import ListView
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator


class IndexView(View):
    template_name = "FINECAP/index.html"

    def get(self, request, *args, **kwargs):
        total_reservas = Reserva.objects.count()
        total_stands = Stand.objects.count()
        context = {
            'total_reservas': total_reservas,
            'total_stands': total_stands,
        }
        return render(request, self.template_name, context)

#---------------------------------------------------------#
#Isso aqui é tipo o listar
def pagination(request):
    reservas = Reserva.objects.all()

    reserva_paginator = Paginator(reservas, 2)
    page_num = request.GET.get('page')
    page = reserva_paginator.get_page(page_num)

    return render(request, 'pagination.html', {'page': page})
#---------------------------------------------------------
class ReservaListView(ListView):
    model = Reserva
    template_name = "reserva/reservas.html"
    context_object_name = 'reservas'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        reservas = Reserva.objects.all()
        context = {
            'reservas': reservas,
        }
        return render(request, self.template_name, context)

#---------------------------------------------------------#

class ReservaCreateView(generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reservas-list")
  template_name = "reserva/form.html"
  
  def form_valid(self, form):
        messages.success(self.request, 'Cadastro realizado com sucesso!')
        return super().form_valid(form)

#---------------------------------------------------------#

class ReservaUpdateView(generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reservas-list")
  template_name = "reserva/form.html"

#---------------------------------------------------------#

class ReservaDeleteView(generic.DeleteView):
    model = Reserva
    template_name = 'reserva/reserva_confirm_delete.html'
    success_url = reverse_lazy("reservas-list")

    def delete(self, request):
        messages.success(self.request, 'Item excluído com sucesso.')
        return super().delete(request)

#---------------------------------------------------------#

def detalhar_reserva(request):
    reservas = Reserva.objects.all()
    context ={
        'reservas':reservas
    }
    return render(request, "reserva/detalhe.html",context)

#------------  Stands  ------------------#

class StandListView(View):
    template_name = "stand/stands.html"

    def get(self, request, *args, **kwargs):
        stands = Stand.objects.all()
        context = {
            'stands': stands,
        }
        return render(request, self.template_name, context)

#---------------------------------------------------------#

class StandCreateView(generic.CreateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stands-list")
  template_name = "stand/form.html"
  
  def form_valid(self, form):
        messages.success(self.request, 'Cadastro de Stand realizado com sucesso!')
        return super().form_valid(form)

#---------------------------------------------------------#

class StandUpdateView(generic.UpdateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stands-list")
  template_name = "stand/form.html"

#---------------------------------------------------------#

class StandDeleteView(generic.DeleteView):
    model = Stand
    template_name = 'stand/stand_confirm_delete.html'
    success_url = reverse_lazy("stands-list")

    def delete(self, request):
        messages.success(self.request, 'Item excluído com sucesso.')
        return super().delete(request)

#---------------------------------------------------------#

#def detalhar_stand(request):
#    stands = Stand.objects.all()
#    context ={
#        'stands':stands
#    }
#    return render(request, "stand/detalhe.html",context)

