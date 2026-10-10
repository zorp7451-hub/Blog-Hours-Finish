from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь', null=True, blank=True)
    about = models.TextField('о себе')
    image = models.ImageField('аватарка', upload_to='photo/', blank=True, null=True)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return f"Профиль {self.user.username if self.user else 'пустой'}"