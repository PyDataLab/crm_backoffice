from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/products-create.html'
    fields = ['name', 'description', 'cost']
    success_url = reverse_lazy('products:product_list')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products-detail.html'
    context_object_name = 'object'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/products-edit.html'
    fields = ['name', 'description', 'cost']
    success_url = reverse_lazy('products:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:product_list')