# Generated by Django 5.0.1 on 2024-03-21 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_clothingsizepants_clothingsizeshirts'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Large')], max_length=3)),
                ('waist', models.CharField(max_length=20)),
                ('length', models.IntegerField()),
                ('image', models.ImageField(upload_to='sizechart/')),
            ],
        ),
        migrations.CreateModel(
            name='FieldData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=1000)),
                ('chart', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.sizechart')),
            ],
        ),
    ]
