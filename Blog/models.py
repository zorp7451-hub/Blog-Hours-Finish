from django.db import models
from accounts.models import User
# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    title = models.CharField('название', max_length=50)
    def __str__(self):
        return self.title


class Tags(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    title = models.CharField('название', max_length=50)
    def __str__(self):
        return self.title

class Blogs(models.Model):
    STATUS_CHOICES = (
        ('draft','черновик'),
        ('under_review','на проверке'),
        ('published','опубликованно'),
        ('rejected','отклонено')
    )
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField('загаловок', max_length=50)
    text = models.TextField('текст')
    category = models.ForeignKey(Category,verbose_name='категория',on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags,verbose_name='тег',on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='under_review',verbose_name='статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')



class Comment(models.Model):
    blog = models.ForeignKey(Blogs, verbose_name='задача',on_delete= models.CASCADE)
    user = models.ForeignKey(User,verbose_name='пользователь',on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')

    parent = models.ForeignKey('self', null = True, blank= True, on_delete= models.CASCADE,verbose_name='родитель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    class Meta:
        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'

    def __str__(self):
        return f"Комментарий от {self.user.username} к '{self.blog.title}'"