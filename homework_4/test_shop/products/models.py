from django.db import models


class Products(models.Model):
    UNIT_CHOICES = (
        ('RUB', 'рубль'),
        ('CNY', 'юань'),
        ('USD', 'доллар'),
        ('EUR', 'евро'),
    )

    title = models.CharField(verbose_name='название',
                             max_length=255)
    date_receipt = models.DateTimeField(verbose_name='дата поступления',
                                        auto_created=True,
                                        auto_now_add=True)
    price = models.PositiveIntegerField(verbose_name='цена',
                                        default=0)
    unit = models.CharField(verbose_name='единица измерения',
                            choices=UNIT_CHOICES,
                            max_length=15)
    supplier = models.CharField(verbose_name='имя поставщика',
                                max_length=255)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
