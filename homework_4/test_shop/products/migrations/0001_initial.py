# Generated by Django 4.2 on 2023-04-25 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_receipt', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='дата поступления')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='цена')),
                ('unit', models.CharField(choices=[('RUB', 'рубль'), ('CNY', 'юань'), ('USD', 'доллар'), ('EUR', 'евро')], max_length=15, verbose_name='единица измерения')),
                ('supplier', models.CharField(max_length=255, verbose_name='имя поставщика')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]