from django.db import models
from django.contrib.auth.models import User
from django.forms import *
from join.models import *

# Create your models here.
class Calculartor(models.Model) :
    work_time = models.IntegerField() #일한 총 시간
    wage = models.IntegerField() #시급

    pay = models.IntegerField() #수당
    holiday_pay = models.IntegerField() #주휴수당
    overtime_pay = models.IntegerField() #야근수당