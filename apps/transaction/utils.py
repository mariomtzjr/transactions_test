from collections import Counter
from typing import final

from apps.company.models import Company

from .models import Transaction


OPEN_API_SUMARY_DATA_EXAMPLE = {
    "total_companies": 162,
    "total_transactions": 2654,
    "paid_payments": {
        "max_paid_payments": {
            "company_name": "rappi",
            "paid_payments_number": 317
        },
        "count": 1393
    },
    "less_paid_payments": {
        "company_name": "omgyes",
        "paid_payments_number": 1
    },
    "rejected_payments": {
        "max_rejected_transactions": {
            "company_name": "uber eats",
            "rejected_transactions_number": 205
        },
        "count": 837
    },
    "total_price_approved": 1857116.0,
    "total_price_no_approved": 21685851.0
}


def get_top_n_companies(companies_number):
    """
    Returns the top 10 companies with the most paid transactions
    """
    transactions = Transaction.objects.all().filter(final_payment=True)
    companies = [transaction.company_id.name for transaction in transactions]
    counter_companies_dict = Counter(companies)
    
    top_n_companies = counter_companies_dict.most_common(companies_number)
    top_n_companies_data = {item[0]: item[1] for item in top_n_companies}
    
    return top_n_companies_data


def build_data(companies_number):
    response_data = {}
    key_for_dict = f"top_{companies_number}_companies"


    response_data[key_for_dict] = {"companies": [{
        'name': company,
        'paid_payments_number': payments_number
        } for company, payments_number in get_top_n_companies(companies_number).items()
    ]}

    return response_data


def get_sumary_data():

    approved_transactions = Transaction.objects.all().filter(final_payment=True)
    non_approved_transactions = Transaction.objects.all().filter(final_payment=False)
    rejected_transactions = Transaction.objects.all().filter(status_approved=False)

    companies = [transaction.company_id.name for transaction in approved_transactions]
    companies_rejected = [transaction.company_id.name for transaction in rejected_transactions]
    
    total_approved_transactions = sum([transaction.price for transaction in approved_transactions])
    total_non_approved_transactions = sum([transaction.price for transaction in non_approved_transactions])

    counter_companies_dict = Counter(companies)
    counter_rejected_companies_dict = Counter(companies_rejected)
    

    company_max_rejected_transactions = counter_rejected_companies_dict.most_common(1)
    company_max_paid_payments = counter_companies_dict.most_common(1)
    company_less_payments = sorted(counter_companies_dict, key=lambda x: counter_companies_dict[x])[0]

    company_max_paid_payments_data = {
        "max_paid_payments": {
            "company_name": company_max_paid_payments[0][0],
            "paid_payments_number": company_max_paid_payments[0][1]
        },
        "count": approved_transactions.count()
    }

    company_less_paid_payments_data = {
        "company_name": company_less_payments,
        "paid_payments_number": dict(counter_companies_dict)[company_less_payments]
    }

    rejected_transactions_data = {
        "max_rejected_transactions": {
            "company_name": company_max_rejected_transactions[0][0],
            "rejected_transactions_number": company_max_rejected_transactions[0][1]
        },
        "count": rejected_transactions.count()
    }

    sumary_data = {}
    sumary_data["total_companies"] = Company.objects.all().count()
    sumary_data["total_transactions"] = Transaction.objects.all().count()
    
    sumary_data["paid_payments"] = company_max_paid_payments_data
    sumary_data["less_paid_payments"] = company_less_paid_payments_data
    
    sumary_data["rejected_payments"] = rejected_transactions_data

    sumary_data["total_price_approved"] = total_approved_transactions
    sumary_data["total_price_no_approved"] = total_non_approved_transactions

    return sumary_data