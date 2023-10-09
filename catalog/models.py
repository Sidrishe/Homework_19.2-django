from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=250, **NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, **NULLABLE, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(**NULLABLE, verbose_name='Цена')
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} : {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=50, verbose_name='Номер версии', **NULLABLE)
    version_name = models.CharField(max_length=50, verbose_name='Название версии')
    is_active = models.BooleanField(verbose_name='Признак текущей версии', default=False)

    def __str__(self):
        return f'{self.version_number} - {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
