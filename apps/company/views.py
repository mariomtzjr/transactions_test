from rest_framework import generics
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from apps.company.models import Company
from apps.company.serializers import CompanySerializer, CompanyDetailSerializer
from .utils import build_instance_data, OPEN_API_COMPANY_DATA_EXAMPLE


# Create your views here.
class CompaniesListAPIView(generics.ListAPIView):
    """Returns the list of companies showing its name and status."""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


class CompanyDetailAPIView(generics.RetrieveAPIView):
    """Returns the detail of a company. Works with the company's id."""

    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "uuid"
    
    @extend_schema(
        # extra parameters added to the schema
        responses={200: CompanyDetailSerializer},
        methods=["GET"],
        # override default docstring extraction
        description="""Returns the detail of a company. Works with the company's id"""
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_data = build_instance_data(instance)

        return Response(instance_data)
