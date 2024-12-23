from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from .models import Advertisement

class AdListView(ListView):
    model = Advertisement
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'

class AdCreateView(CreateView):
    model = Advertisement
    template_name = 'ads/ads-create.html'
    fields = ['name', 'product', 'budget']
    success_url = reverse_lazy('ads:list')

class AdDetailView(DetailView):
    model = Advertisement
    template_name = 'ads/ads-detail.html'
    context_object_name = 'object'

class AdUpdateView(UpdateView):
    model = Advertisement
    template_name = 'ads/ads-edit.html'
    fields = ['name', 'product', 'budget']
    success_url = reverse_lazy('ads:list')

class AdDeleteView(DeleteView):
    model = Advertisement
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:list')

class AdStatisticView(TemplateView):
    template_name = 'ads/ads-statistic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ads = Advertisement.objects.all()
        for ad in ads:
            ad.leads_count = ad.product.leads.count() if hasattr(ad.product, 'leads') else 0
            ad.customers_count = ad.product.customers.count() if hasattr(ad.product, 'customers') else 0
            ad.profit = ad.budget / ad.leads_count if ad.leads_count else None
        context['ads'] = ads
        return context