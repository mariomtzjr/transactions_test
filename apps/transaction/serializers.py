from rest_framework import serializers

from .models import Transaction, TransactionStatus


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id', 'company_id', 'price', 'date',
            'status_transaction', 'status_approved', 'final_payment',
        ]


class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = ['id', 'name', 'description']
        