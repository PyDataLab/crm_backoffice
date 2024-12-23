# Generated by Django 5.1.4 on 2024-12-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('operator', 'Оператор'), ('marketer', 'Маркетолог'), ('manager', 'Менеджер')], default='operator', max_length=20, verbose_name='Роль'),
        ),
    ]
