from django.db import models

from payment.choices import PAYABLE_STATUS, PAY_METHODS


class Payable(models.Model):
    bar_code = models.CharField(max_length=48, primary_key=True, unique=True)
    service_type = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    expiration_date = models.DateField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=1, choices=PAYABLE_STATUS)

    class Meta:
        verbose_name = "Payable"
        verbose_name_plural = "Payables"


class Transaction(models.Model):
    payable = models.OneToOneField(Payable, on_delete=models.SET_NULL, null=True)
    method = models.CharField(max_length=15, choices=PAY_METHODS)
    card_number = models.CharField(max_length=19, blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    payment_date = models.DateField()

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
