from django.db import models

# Create your models here.
class Maker(models.Model):
    mname = models.CharField(max_length=10)
    tel = models.CharField(max_length = 30)
    addr = models.CharField(max_length = 50)
    
    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.mname # mname을 자동으로 참조하게 만든다.
        
class Product(models.Model):        
    pname = models.CharField(max_length = 10)
    price = models.IntegerField()
    maker_name = models.ForeignKey(Maker, on_delete=models.CASCADE) # maker의 mname컬럼을 참조한다.
    