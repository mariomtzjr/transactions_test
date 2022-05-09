from rest_framework import generics
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from apps.company.models import Company
from apps.company.serializers import CompanySerializer, CompanyDetailSerializer
from .utils import build_instance_data, COMPANY_DATA, OPEN_API_COMPANY_DATA_EXAMPLE


# Create your views here.
class CompaniesListAPIView(generics.ListAPIView):
    """Returns the list of companies showing its name and status."""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


    @extend_schema(
        responses={200: CompanySerializer},
        methods=["GET"],
        parameters=[
            OpenApiParameter(
                name='country_code',
                location=OpenApiParameter.QUERY,
                required=False,
                type=str,
                examples=[
                    OpenApiExample(
                        'Filter by country code',
                        value='MX'
                    ),
                ],
            ),
            OpenApiParameter(
                name='zip_code',
                location=OpenApiParameter.QUERY,
                required=False,
                type=str,
                examples=[
                    OpenApiExample(
                        'Filter by zip_code',
                        value='09840'
                    ),
                ],
            ),
        ],
        description="""Returns the list of companies showing its name and status.""",
        examples=[
            OpenApiExample(
                'Example 1',
                description='GET /api/v1/companies/?country_code=MX',
                value=COMPANY_DATA
            ),
            OpenApiExample(
                'Example 2',
                description='GET /api/v1/companies/?zip_code=09840',
                value=COMPANY_DATA
            ),
            OpenApiExample(
                'Example 3',
                description='GET /api/v1/companies/',
                value=COMPANY_DATA
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        if request.query_params:
            if request.query_params.get("country_code"):
                query_param = request.query_params.get("country_code")
                queryset_by_country_code = self.get_queryset().filter(address__country_code_id__country_code=query_param)
                serializer = CompanySerializer(queryset_by_country_code, many=True)
                return Response(serializer.data)
            if request.query_params.get("zip_code"):
                query_param = request.query_params.get("zip_code")
                queryset_by_zip_code = self.get_queryset().filter(address__zip_code=query_param)
                serializer = CompanySerializer(queryset_by_zip_code, many=True)
                return Response(serializer.data)
            
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
