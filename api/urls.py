from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from apps.transaction.views import TransactionsDetailViewSet, TransactionsListAPIView
from apps.company.views import CompaniesListAPIView, CompanyDetailAPIView


urlpatterns = [
    path('sumary/', TransactionsDetailViewSet.as_view({'get': 'list'}), name='transactions_detail'),

    # Companies list
    path('companies/', CompaniesListAPIView.as_view(), name='companies_list'),
    path('companies/<uuid:uuid>', CompanyDetailAPIView.as_view(), name='companies_detail'),

    # Transactions list
    path('transactions/', TransactionsListAPIView.as_view(), name='transactions_list'),

    # Doenload API schema
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]