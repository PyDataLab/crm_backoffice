from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('operator', 'Оператор'),
        ('marketer', 'Маркетолог'),
        ('manager', 'Менеджер'),
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='operator',
        verbose_name="Роль"
    )

    def is_admin(self):
        return self.role == 'admin'

    def is_operator(self):
        return self.role == 'operator'

    def is_marketer(self):
        return self.role == 'marketer'

    def is_manager(self):
        return self.role == 'manager'
