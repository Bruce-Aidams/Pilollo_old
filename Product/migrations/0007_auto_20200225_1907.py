# Generated by Django 2.0.2 on 2020-02-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_auto_20200225_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_rate',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
