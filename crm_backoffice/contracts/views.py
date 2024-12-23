from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Contract

class ContractListView(ListView):
    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'

class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'
    context_object_name = 'object'

class ContractCreateView(CreateView):
    model = Contract
    template_name = 'contracts/contracts-create.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('contracts:list')

class ContractUpdateView(UpdateView):
    model = Contract
    template_name = 'contracts/contracts-edit.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('contracts:list')

class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('contracts:list')