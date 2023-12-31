# Generated by Django 4.2.6 on 2023-10-24 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prod_image', models.ImageField(upload_to='product_image/')),
                ('old_price', models.PositiveBigIntegerField()),
                ('new_price', models.PositiveBigIntegerField()),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.catagory')),
            ],
        ),
    ]
