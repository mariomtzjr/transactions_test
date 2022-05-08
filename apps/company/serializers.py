from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'company_estatus']


class TransactionDataSerializer(serializers.Serializer):
    data = serializers.DictField(
        child=serializers.DictField()
    )


class CompanyDetailSerializer(serializers.Serializer):
    id = serializers.SlugField()
    name = serializers.CharField()
    status = serializers.CharField()
    transactions = serializers.DictField(
        child=serializers.DictField()
    )


