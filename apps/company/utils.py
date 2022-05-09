from collections import Counter

from apps.transaction.models import Transaction
from apps.transaction.utils import OPEN_API_SUMARY_DATA_EXAMPLE

OPEN_API_COMPANY_DATA_EXAMPLE = {
    "id": "38e657b1-ea73-42d9-bc15-9d9c532fbc0e",
    "name": "rappi",
    "status": "active",
    "address": {
        "street": "Cuauhtemoc",
        "number": "324",
        "colony": "Los Reyes",
        "city": "CDMX",
        "state": "Iztapalapa",
        "country_code": "MX",
        "zip_code": "09840"
    },
    "financial_data": {
        "accounts": [
            {
                "clabe": "12345678911122234",
                "account_number": "12345678",
                "account_type": "Inversion"
            }
        ]
    },
    "transactions": {
        "data": {
            "paid_payments": 317,
            "no_paid_payments": 247,
            "max_transactions_data": {
                "date": "2021-05-24",
                "count": 32
            }
        },
        "count": 564
    }
}

COMPANY_DATA = [
    {
        "id": "38e657b1-ea73-42d9-bc15-9d9c532fbc0e",
        "name": "rappi",
        "company_estatus": "active"
    }
]


def get_dates_from_instance(instance):
    transactions = Transaction.objects.filter(company_id=instance.id)
    dates = [transaction.date.strftime("%Y-%m-%d") for transaction in transactions]

    return dates


def get_number_transactions_per_day(dates):
    max_transactions_per_day = max(Counter(dates), key = lambda k: Counter(dates)[k])

    return max_transactions_per_day


def build_instance_data(instance):
    instance_data = {}
    instance_data["id"] = instance.id
    instance_data["name"] = instance.name
    instance_data["status"] = instance.company_estatus
    instance_data["address"] = {
        "street": instance.address.street or "",
        "number": instance.address.number or "",
        "colony": instance.address.colony or "",
        "city": instance.address.city or "",
        "state": instance.address.state or "",
        "country_code": instance.address.country_code_id.country_code or "",
        "zip_code": instance.address.zip_code or ""
    }
    instance_data["financial_data"] = {
        "accounts": [
            {
                "clabe": account.clabe,
                "account_number": account.account_number,
                "account_type": account.account_type.type_name
            }
        ] for account in instance.account_set.all()
    }
        
    instance_data["transactions"] = {"data": {}}
    instance_data["transactions"]["count"] = Transaction.objects.filter(company_id=instance.id).count()
    instance_data["transactions"]["data"]["paid_payments"] = Transaction.objects.filter(company_id=instance.id, final_payment=True).count()
    instance_data["transactions"]["data"]["no_paid_payments"] = Transaction.objects.filter(company_id=instance.id, final_payment=False).count()
    
    max_transactions_per_day = get_number_transactions_per_day(get_dates_from_instance(instance))

    instance_data["transactions"]["data"]["max_transactions_data"] = {
        "date": max_transactions_per_day,
        "count": get_dates_from_instance(instance).count(max_transactions_per_day)
    }

    return instance_data