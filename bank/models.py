from django.db import models

class Bank(models.Model):
    bank_id = models.BigAutoField(primary_key=True)  
    name = models.CharField(max_length=49)
    

    def __str__(self):
        return self.name

class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=74)
    address = models.CharField(max_length=195)  
    city = models.CharField(max_length=50)  
    district = models.CharField(max_length=50) 
    state = models.CharField(max_length=26)  

    def __str__(self):
        return self.branch_name


class AllData(models.Model):
    ifsc = models.CharField(max_length=11)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name
