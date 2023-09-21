from django.db import models


class User(models.Model):
    def __str__(self):
        return f'Имя пользователя: {self.user_name}, идентификатор: {self.user_id}'

    user_id = models.BigAutoField(primary_key=True, verbose='Идентификатор пользователя')
    user_name = models.CharField(max_length=30, verbose='Имя пользователя')


class Owner(models.Model):
    def __str__(self):
        return f'Имя владельца: {self.owner_name}, идентификатор: {self.owner_id}'

    owner_id = models.BigAutoField(primary_key=True, verbose='Идентификатор владельца')
    owner_name = models.CharField(max_length=30, verbose='Имя Владельца')


class Lesson(models.Model):
    def __str__(self):
        return f'Идентификатор урока: {self.lesson_id}, длина урока: {self.length}'

    lesson_id = models.BigAutoField(primary_key=True, verbose='Идентификатор урока')
    link = models.CharField(max_length=100, verbose='Ссылка на видео')
    length = models.TimeField(verbose='Продолжительность видео')


class Product(models.Model):
    def __str__(self):
        return f'Имя продукта: {self.product_name}, идентификатор: {self.product_id}, идентификатор владельца: {self.owner_id}'

    product_id = models.BigAutoField(primary_key=True, verbose='Идентификатор продукта')
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose='Идентификатор владельца')
    product_name = models.CharField(max_length=30, verbose='Имя продукта')


class ProductCompound(models.Model):
    def __str__(self):
        return f'Идентификатор продукта: {self.product_id}, идентификатор урока: {self.lesson_id}'

    product_id = models.ForeignKey(Product, primary_key=True, on_delete=models.CASCADE, verbose='Идентификатор продукта')
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose='Идентификатор урока')


class Access(models.Model):
    def __str__(self):
        return f'Идентификатор пользователя: {self.user_id}, Идентификатор продукта: {self.product_id}'

    product_id = models.ForeignKey(Product, primary_key=True, on_delete=models.CASCADE, verbose='Идентификатор продукта')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose='Идентификатор пользователя')


class UserProgress(models.Model):
    def __str__(self):
        return f'Идентификатор пользователя: {self.user_id}, Идентификатор урока: {self.lesson_id}, Просмотрено: {self.time_progress},' \
               f'Считается изученным: {self.watched}'

    user_id = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE, verbose='Идентификатор пользователя')
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose='Идентификатор урока')
    time_progress = models.TimeField(verbose='Длительность просмотра')
    watched = models.BooleanField('Идентификатор пользователя', default=False)

