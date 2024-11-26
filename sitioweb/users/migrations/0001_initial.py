# Generated by Django 5.1.3 on 2024-11-06 15:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='personal_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100, verbose_name='Nombres')),
                ('last_names', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('position', models.CharField(max_length=100, verbose_name='cargo')),
                ('date', models.DateField(blank=True, null=True, verbose_name='fecha')),
                ('description', models.CharField(max_length=100, verbose_name='descripción')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='fecha')),
                ('update_at', models.DateField(auto_now=True, null=True, verbose_name='fecha')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Informacion Personal',
                'verbose_name_plural': 'Informaciones Personales',
            },
        ),
    ]