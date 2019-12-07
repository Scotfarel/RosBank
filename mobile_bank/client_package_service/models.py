from django.db import models


class Companies(models.Model):
    owner_id = models.IntegerField()
    name = models.CharField(max_length=1024)
    cash_flow = models.BigIntegerField()
    number_of_employees = models.BigIntegerField()
    confidence_ratio = models.FloatField()

    def __str__(self):
        return f'{self.name} {self.cash_flow} {self.number_of_employees}'


class CompanySettings(models.Model):
    company_id = models.IntegerField()
    time_interval = models.BooleanField()
    billing_enable = models.BooleanField()
    enable_error_name_payment = models.BooleanField()
    files_format = models.CharField(max_length=10)

