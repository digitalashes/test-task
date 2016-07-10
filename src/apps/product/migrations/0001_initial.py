# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 19:20
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=3)], verbose_name='Name')),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=3)], verbose_name='Url')),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(limit_value=3)], verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=3)], verbose_name='Name')),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=3)], verbose_name='Url')),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(limit_value=3)], verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.CategoryModel', verbose_name='Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'verbose_name': 'Product',
            },
        ),
    ]
