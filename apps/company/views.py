import uuid
from collections import Counter

from django.shortcuts import render, get_object_or_404

from rest_framework import generics
from rest_framework.response import Response

from apps.company.models import Company
from apps.company.serializers import CompanySerializer
from apps.transaction.models import Transaction


# Create your views here.
class CompaniesListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "id"
    lookup_url_kwarg = "uuid"
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        
        instance_data = {}
        instance_data["id"] = instance.id
        instance_data["name"] = instance.name
        instance_data["status"] = instance.company_estatus
        
        instance_data["transactions"] = {"data": {}}
        instance_data["transactions"]["count"] = Transaction.objects.filter(company_id=instance.id).count()
        instance_data["transactions"]["data"]["paid_payments"] = Transaction.objects.filter(company_id=instance.id, final_payment=True).count()
        instance_data["transactions"]["data"]["no_paid_payments"] = Transaction.objects.filter(company_id=instance.id, final_payment=False).count()

        transactions = Transaction.objects.filter(company_id=instance.id)
  
        dates = [transaction.date.strftime("%Y-%m-%d") for transaction in transactions]
        max_transactions_per_day = max(Counter(dates), key = lambda k: Counter(dates)[k])
        
        instance_data["transactions"]["data"]["max_transactions_data"] = {
            "date": max_transactions_per_day,
            "count": dates.count(max_transactions_per_day)
        }

        return Response(instance_data)
