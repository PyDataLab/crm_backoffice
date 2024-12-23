from django.shortcuts import render
from products.models import Product
from ads.models import Advertisement
from leads.models import Lead
from customers.models import Customer

# Функция для отображения главной страницы
def index(request):
    # Получение количества данных из базы
    products_count = Product.objects.count()
    advertisements_count = Advertisement.objects.count()
    leads_count = Lead.objects.count()
    customers_count = Customer.objects.count()

    context = {
        'products_count': products_count,
        'advertisements_count': advertisements_count,
        'leads_count': leads_count,
        'customers_count': customers_count,
    }

    return render(request, 'users/index.html', context)
