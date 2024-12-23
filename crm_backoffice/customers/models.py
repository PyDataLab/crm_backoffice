from django.db import models
from django.urls import reverse
from leads.models import Lead

class Customer(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, related_name='customer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.lead.last_name} {self.lead.first_name}"

    def get_absolute_url(self):
        return reverse('customers:customer-detail', kwargs={'pk': self.pk})
