from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('core.urls')),
    path('', include('users.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('ads/', include('ads.urls')),
    path('leads/', include('leads.urls')),
    path('contracts/', include('contracts.urls')),
    path('customers/', include('customers.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
