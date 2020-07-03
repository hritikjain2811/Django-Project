from django.db import models

class accounts(models.Model):
    ifsc_code = models.CharField(max_length=15, null=False)
    branch_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=300, null=False)
    city = models.CharField(max_length=80, null=False)
    bank_name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.ifsc_code
