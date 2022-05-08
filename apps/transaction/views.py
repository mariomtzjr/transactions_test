from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer
from .utils import build_data


# Create your views here.
class TransactionsListAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        
        if self.request.query_params.get('top'):
            top_number = int(self.request.query_params.get('top'))
        else:
            top_number = 5

        data = build_data(top_number)

        return Response(data)