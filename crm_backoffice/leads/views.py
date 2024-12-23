from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Lead

class LeadListView(ListView):
    model = Lead
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'

class LeadCreateView(CreateView):
    model = Lead
    template_name = 'leads/leads-create.html'
    fields = ['first_name', 'last_name', 'phone', 'email']
    success_url = reverse_lazy('leads:lead_list')

class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'

class LeadUpdateView(UpdateView):
    model = Lead
    template_name = 'leads/leads-edit.html'
    fields = ['first_name', 'last_name', 'phone', 'email']
    success_url = reverse_lazy('leads:lead_list')

class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:lead_list')