from rest_framework import serializers

from payment.models import Payable
from payment.models import Transaction


class PayableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payable
        fields = '__all__'
        extra_kwargs = {'description': {'write_only': True}, 'status': {'write_only': True}}


class PayableSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = Payable
        fields = ['expiration_date', 'amount' ,'bar_code']


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'