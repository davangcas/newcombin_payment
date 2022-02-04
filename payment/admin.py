from django.contrib import admin

from payment.models import Payable, Transaction


admin.site.register(Payable)
admin.site.register(Transaction)