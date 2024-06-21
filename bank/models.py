from django.db import models 

class Bank(models.Model):
    bank_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.name 
    
class Branch(models.Model):
    ifsc = models.CharField(max_length=11,primary_key=True)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.branch_name