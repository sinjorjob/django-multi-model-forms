from django.db import models
from django.core.validators import RegexValidator

class Employee(models.Model):
    class Meta:
        verbose_name ="社員"
        verbose_name_plural ="社員"

    name = models.CharField(verbose_name="名前", max_length=50)
    age = models.IntegerField(verbose_name="年齢")

    def __str__(self):
        return self.name


class MynumberCard(models.Model):
    class Meta:
        verbose_name ="マイナンバー"
        verbose_name_plural ="マイナンバー"
    number = models.IntegerField(verbose_name ='マイナンバー')
    employee = models.OneToOneField(Employee, on_delete = models.PROTECT,verbose_name ="社員名")

    def __str__(self):
        return str(self.number)


class Contact(models.Model):
    class Meta:
        verbose_name ="連絡先"
        verbose_name_plural ="連絡先"

    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("携帯の電話番号を入力してください。 例：'09012345678'"))
    phoneNumber = models.CharField(validators=[tel_number_regex], max_length=11, verbose_name='電話番号')
    address = models.CharField(verbose_name='住所', max_length=250)
    employee = models.OneToOneField(Employee, on_delete = models.PROTECT,verbose_name ="社員名")


    def __str__(self):
        return self.employee.name
