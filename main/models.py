from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
