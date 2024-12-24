from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Customer
from .forms import CustomerForm

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/customers-create.html'
    form_class = CustomerForm

    def get_success_url(self):
        return reverse_lazy('customers:customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customers-edit.html'
    form_class = CustomerForm

    def get_success_url(self):
        return reverse_lazy('customers:customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'

    def get_success_url(self):
        return reverse_lazy('customers:customer-list')
