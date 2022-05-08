from rest_framework import generics
from rest_framework.response import Response

from apps.company.models import Company
from apps.company.serializers import CompanySerializer
from .utils import build_instance_data


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
        instance_data = build_instance_data(instance)

        return Response(instance_data)
