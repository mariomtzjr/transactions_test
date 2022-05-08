from collections import Counter

from .models import Transaction


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