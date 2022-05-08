from collections import Counter

from apps.transaction.models import Transaction


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