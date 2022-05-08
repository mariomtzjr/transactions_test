from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from .models import Transaction
from .serializers import TransactionSerializer, SummarySerializer
from .utils import build_data, get_sumary_data, OPEN_API_SUMARY_DATA_EXAMPLE


# Create your views here.
class TransactionsListAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionsDetailViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for show sumary transactions data. This endpoint has enabled
    top query_parameter to get N number of companies to show most paid transactions.
    """

    @extend_schema(
        # extra parameters added to the schema
        responses={200: SummarySerializer},
        methods=["GET"],
        parameters=[
            OpenApiParameter(
                name='top',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Filter by top N companies with the most paid transactions. Example: /api/v1/sumary/?top=5',
                examples=[
                    OpenApiExample(
                        'Example 1',
                        summary='Top 5 companies with the most paid transactions',
                        description='Top 5 companies with the most paid transactions',
                        value='5'
                    ),
                ],
            ),
        ],
        # override default docstring extraction
        description="""A simple ViewSet for show sumary transactions data. This endpoint has enabled
        top query_parameter to get N number of companies to show the most paid transactions.""",
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                'Example 1',
                description='Response example for sumary transactions data',
                value=OPEN_API_SUMARY_DATA_EXAMPLE
            ),
        ],
    )
    def list(self, request):
        if self.request.query_params:
            top_number = int(self.request.query_params.get('top'))
            data = build_data(top_number)

            return Response(data)
        
        data = get_sumary_data()


        return Response(data)


class TransactionDetailAPIView(generics.RetrieveAPIView):
    """Returns the detail of a transaction. Works with the transaction's id."""

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "id"
    lookup_url_kwarg = "uuid"

    