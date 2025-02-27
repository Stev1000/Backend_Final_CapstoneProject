# Generated by Django 5.1.4 on 2025-01-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=100)),
                ('stock_quantity', models.PositiveIntegerField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
