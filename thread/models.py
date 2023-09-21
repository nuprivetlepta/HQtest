from django.db import models


class User(models.Model):
    def __str__(self):
        return f'Имя пользователя: {self.user_name}, идентификатор: {self.user_id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_id = models.BigAutoField(primary_key=True, verbose_name='Идентификатор пользователя')
    user_name = models.CharField(max_length=30, verbose_name='Имя пользователя')


class Owner(models.Model):
    def __str__(self):
        return f'Имя владельца: {self.owner_name}, идентификатор: {self.owner_id}'

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

    owner_id = models.BigAutoField(primary_key=True, verbose_name='Идентификатор владельца')
    owner_name = models.CharField(max_length=30, verbose_name='Имя Владельца')


class Lesson(models.Model):
    def __str__(self):
        return f'Идентификатор урока: {self.lesson_id}, длина урока: {self.length}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    lesson_id = models.BigAutoField(primary_key=True, verbose_name='Идентификатор урока')
    link = models.CharField(max_length=100, verbose_name='Ссылка на видео')
    length = models.TimeField(verbose_name='Продолжительность видео')


class Product(models.Model):
    def __str__(self):
        return f'Имя продукта: {self.product_name}, идентификатор: {self.product_id}, идентификатор владельца: {self.owner_id}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    product_id = models.BigAutoField(primary_key=True, verbose_name='Идентификатор продукта')
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='Идентификатор владельца')
    product_name = models.CharField(max_length=30, verbose_name='Имя продукта')


class ProductCompound(models.Model):
    def __str__(self):
        return f'Идентификатор продукта: {self.product_id}, идентификатор урока: {self.lesson_id}'

    class Meta:
        verbose_name = 'Состав продукта'
        verbose_name_plural = 'Составы продуктов'

    product_id = models.ForeignKey(Product, primary_key=True, on_delete=models.CASCADE, verbose_name='Идентификатор продукта')
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Идентификатор урока')


class Access(models.Model):
    def __str__(self):
        return f'Идентификатор пользователя: {self.user_id}, Идентификатор продукта: {self.product_id}'

    class Meta:
        verbose_name = 'Доступ'
        verbose_name_plural = 'Права доступа'

    product_id = models.ForeignKey(Product, primary_key=True, on_delete=models.CASCADE, verbose_name='Идентификатор продукта', unique=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Идентификатор пользователя')


class UserProgress(models.Model):
    def __str__(self):
        return f'Идентификатор пользователя: {self.user_id}, Идентификатор урока: {self.lesson_id}, Просмотрено: {self.time_progress},' \
               f'Считается изученным: {self.watched}'

    class Meta:
        verbose_name = 'Индикатор прогресса'
        verbose_name_plural = 'Индикаторы прогресса'

    user_id = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE, verbose_name='Идентификатор пользователя')
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Идентификатор урока')
    time_progress = models.TimeField(verbose_name='Длительность просмотра')
    watched = models.BooleanField('Идентификатор пользователя', default=False)

