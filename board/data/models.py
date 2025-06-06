from django.db import models

# Create your models here.

class Personal_Data(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    speciality = models.CharField(max_length=255, verbose_name="Специальность")
    room = models.IntegerField(verbose_name="Кабинет", unique=True)
    time = models.TimeField(verbose_name="Время приёма")

    def __str__(self):
        return f'Врач {self.speciality} {self.name} принимает в {self.room} кабинете в {self.time}'

    class Meta:
        verbose_name = "Данные врача"
        verbose_name_plural = "Данные врачей"
