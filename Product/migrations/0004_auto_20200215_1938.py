# Generated by Django 2.0.2 on 2020-02-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20200215_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='back_view',
            field=models.ImageField(blank=True, default=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'), upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='left_view',
            field=models.ImageField(blank=True, default=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'), upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='right_view',
            field=models.ImageField(blank=True, default=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'), upload_to='products/%Y/%m/%d'),
        ),
    ]