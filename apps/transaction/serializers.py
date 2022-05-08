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


class SummarySerializer(serializers.Serializer):
    total_companies = serializers.IntegerField()
    total_transactions = serializers.IntegerField()
    paid_payments = serializers.DictField(
        child=serializers.DictField(
        )
    )
    less_paid_payments = serializers.DictField(
        child=serializers.DictField()
    )
    rejected_payments = serializers.DictField(
        child=serializers.DictField()
    )
    total_price_approved = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_price_non_approved = serializers.DecimalField(max_digits=10, decimal_places=2)