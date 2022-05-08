from django.urls import path

from apps.transaction.views import TransactionDetailViewSet, TransactionsListAPIView
from apps.company.views import CompaniesListAPIView, CompanyDetailAPIView


urlpatterns = [
    path('sumary/', TransactionDetailViewSet.as_view({'get': 'list'}), name='transactions_detail'),

    # Companies list
    path('companies/', CompaniesListAPIView.as_view(), name='companies_list'),
    path('companies/<uuid:uuid>', CompanyDetailAPIView.as_view(), name='companies_detail'),

    # Transactions list
    path('transactions/', TransactionsListAPIView.as_view(), name='transactions_list'),
]