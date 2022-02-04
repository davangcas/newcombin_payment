from django.urls import path
from payment import views

app_name = "payment"

urlpatterns = [
    path('payables', views.PayableAPIView.as_view(), name="payables"),
    path('transactions', views.TransactionAPIView.as_view(), name="transactions")
]