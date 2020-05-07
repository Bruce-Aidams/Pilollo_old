# Generated by Django 2.0.2 on 2020-02-15 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'catalog',
                'verbose_name_plural': 'catalogs',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='category',
            name='catalog',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='catalogs', to='Product.Catalog'),
        ),
    ]