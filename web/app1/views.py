
from django.views.generic import TemplateView, CreateView,ListView,UpdateView, DeleteView, DetailView, FormView
from app1.models import Cliente
from django.urls import reverse
from app1.forms import DireccionForm, AdjuntoForm

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['identificacion', 'nombre']
    def get_success_url(self, **kwargs):     
            return reverse('list_clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['identificacion', 'nombre']
    def get_success_url(self, **kwargs):     
            return reverse('list_clientes')

class ClienteDetailView(DetailView):
    model = Cliente
    def get_success_url(self, **kwargs):     
            return reverse('list_clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    def get_success_url(self, **kwargs):     
            return reverse('list_clientes')

class ClienteListView(ListView):
    model = Cliente

class DireccionView(FormView):
    form_class= AdjuntoForm
    template_name = "direccion.html"
    def get_success_url(self, **kwargs):     
            return reverse('list_clientes')


class EjemploTemplateView(TemplateView):
    template_name="template.html"

    def get_context_data(self, **kwargs):
        context = super(EjemploTemplateView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET
        return context