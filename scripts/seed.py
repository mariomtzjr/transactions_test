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
                final_payment=row.final_payment,
            )
        except Exception as e:
            print(e)


def populate_database_companies():
    print("Populating database with companies...")

    df = get_dataframe()
        
    for row in df.itertuples():
        try:
            Company.objects.create(
                id=row.company_id,
                name=row.company,
                company_estatus='active',
            )
        except Exception as e:
            print(e)
            print(f"{row.company} already exists in the database")
            pass  


def main():
    build_dataframe()
    populate_database_companies()
    populate_database_transactions()


if __name__ == '__main__':
    main()
    