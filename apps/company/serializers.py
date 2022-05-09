from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'company_estatus']


class CompanyDetailSerializer(serializers.Serializer):
    id = serializers.SlugField()
    name = serializers.CharField()
    status = serializers.CharField()
    address = serializers.DictField()
    transactions = serializers.DictField(
        child=serializers.DictField()
    )
    financial_data = serializers.DictField(
        child=serializers.ListField(
            child=serializers.DictField()
        )
    )


