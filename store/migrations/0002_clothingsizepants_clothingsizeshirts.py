# Generated by Django 5.0.1 on 2024-03-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingSizePants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Large')], max_length=3)),
                ('waist', models.CharField(max_length=20)),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClothingSizeShirts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Large')], max_length=3)),
                ('waist', models.CharField(max_length=20)),
                ('length', models.IntegerField()),
            ],
        ),
    ]
