from django.db import models

# Create your models here.

class Coffee(models.Model):
    def __str__(self) :
        return self.name
    # Field 1
    # Field 2 (얘네가 각각 데이터베이스의 column이 됨)
    #field1 = models.FieldType()...
    #field1 = models.FieldType()...
    #field1 = models.FieldType()...
    """
    문자열 : CharField
    숫자 : IntegerField, SmallIntegerField, ...
    논리형 : BooleanField
    시간/날짜: DateTimeField
    ...
    """
    name = models.CharField(default="", max_length=30)
    price =  models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)





