import os
import csv
import sqlite3
from sqlite3 import Error
import uuid
from datetime import datetime

import pandas as pd

from apps.company.models import Company
from apps.transaction.models import Transaction


def build_dataframe():
    df = pd.read_csv("./data/test_database.csv")
    df = df.dropna(axis=0)

    df["company"] = df["company"].str.lower()
    
    try:
        df["company_id"]
    except KeyError:
        company_uuids = [uuid.uuid4() for i in range(len(df))]
        df["company_id"] = company_uuids

    try:
        df["final_payment"]
    except KeyError:
        company_final_payments_status = [
            True if row.status_transaction == "closed" and row.status_approved == True else False for row in df.itertuples()
        ]
        df["final_payment"] = company_final_payments_status
    
    try:
        df["transaction_id"]
    except KeyError:
        transaction_uuids = [uuid.uuid4() for i in range(len(df))]
        df["transaction_id"] = transaction_uuids
    
    df.to_csv("./data/test_database_built.csv", index=False)


def get_dataframe():
    return pd.read_csv("./data/test_database_built.csv")


def populate_database_transactions():
    print("Populating database with transactions...")

    df = get_dataframe()

    for row in df.itertuples():
        try:
            Transaction.objects.create(
                id=row.transaction_id,
                company_id=Company.objects.get(name=row.company),
                price=row.price,
                date=row.date,
                status_transaction=row.status_transaction,
                status_approved=row.status_approved,
                final_payment=row.final_payment
            )
        except Exception as e:
            print(e)


def populate_database_other_instances():
    print("Populating database with other instances...")
    print("Creating AccountType instance...")

    from apps.account.models import Account, AccountType
    from apps.address.models import Address, CountryCode
    from apps.user.models import CompanyUser, UserType, UserContactType
   
    AccountType.objects.create(
        id="4944ff17-a37c-4b0d-9e41-01e4ed30b945",
        type_name="Inversion"
    )

    print("Creating Account instance...")
    Account.objects.create(
        id="ca15dca9-e5c3-4799-bd5b-8232d35ce846",
        clabe="12345678911122234",
        account_number="12345678",
        company_id="38e657b1-ea73-42d9-bc15-9d9c532fbc0e"
    )

    print("Creating CountryCode instance...")
    CountryCode.objects.create(
        id="17257e75-e972-4ba7-82b3-eabe18cac62b",
        country_code="MX",
        country_name="Mexico"
    )

    print("Creating Address instance...")
    Address.objects.create(
        id="2f18c513-43fa-4375-8e89-a97e743900c8",
        company_id="38e657b1-ea73-42d9-bc15-9d9c532fbc0e",
        street="Calle de las Flores",
        number="123",
        colony="Los Reyes",
        city="Iztacalco",
        state="CDMX",
        country_code_id="17257e75-e972-4ba7-82b3-eabe18cac62b",
        zip_code="09876"
    )
    
    print("Creating UserType instance...")
    UserType.objects.create(
        id="9b02e2e7-565b-4a4e-a879-ff90ed2e263d",
        type_name="Owner"
    )
    UserContactType.objects.create(
        id="80a815c0-0d2a-4855-b228-14edaa581855",
        contact_type_name="email",
        contact_type_value="francisco.smtz@gmail.com"
    )
    CompanyUser.objects.create(
        id="cdb18002-412a-4f4c-8092-efd09363a0c1",
        name="Mario",
        lastname="Martinez",
        company_id="38e657b1-ea73-42d9-bc15-9d9c532fbc0e",
        user_type_id="9b02e2e7-565b-4a4e-a879-ff90ed2e263d",
        contact_type_id="80a815c0-0d2a-4855-b228-14edaa581855"
    )


def populate_database_companies():
    print("Populating database with companies...")

    df = get_dataframe()
        
    for row in df.itertuples():
        try:
            Company.objects.create(
                id=row.company_id,
                name=row.company,
                company_estatus='active'
            )
        except Exception as e:
            print(e)
            print(f"{row.company} already exists in the database")
            pass  


def main():
    build_dataframe()
    populate_database_companies()
    populate_database_transactions()
    populate_database_other_instances()


if __name__ == '__main__':
    main()
    