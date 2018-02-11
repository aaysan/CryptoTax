#! /usr/bin/env python

from coinbase.wallet.client import Client
from transactions import Transaction
import json
import add_to_pdf

import sys
import os
os.getcwd()

def readKeys(filename):
    file = open(filename, "r")
    lines = file.readlines()

    api_key = lines[0].strip()
    api_secret = lines[1].strip()

    return api_key, api_secret


def getTransactionsInAllAccounts(api_key, api_secret):
    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        api_version='2017-12-07')
    accounts = client.get_accounts()

    transactions = []

    for account in accounts.data:
        transactions.append(account.get_transactions())

    return transactions


def parseTransactionsInAccount(account):
    account_transactions = []

    for transactions in account['data']:
        date_acquired = "-"
        date_sold = "-"
        if "buy" == transactions["type"]:
            date_acquired = transactions["updated_at"]
        elif "sell" == transactions["type"]:
            date_sold = transactions["updated_at"]
        else:
            continue
        description = transactions["details"]["title"]

        crypto_currency = transactions["amount"]["currency"]
        crypto_amount = transactions["amount"]["amount"]

        proceeds = transactions["native_amount"]["amount"]
        currency = transactions["native_amount"]["currency"]

        current_transaction = Transaction(description, crypto_currency, crypto_amount, date_acquired, date_sold, proceeds, currency)

        account_transactions.append(current_transaction)

    return account_transactions


def parseTransactions(transactions):
    allTransactions = []
    for account in transactions:
        allTransactions.extend(parseTransactionsInAccount(account))
    return allTransactions


# def printTransactions(account):
#     for transactions in account:
#         transactions.print()
#     return


def printInFileAsJSON(transactions):
    jsonTransactions = json.dumps([transaction.__dict__ for transaction in transactions])
    print(jsonTransactions)
    filename = "transactions.json"
    file = open(filename, "w")
    file.writelines(jsonTransactions)


def main():
    api_key, api_secret = readKeys("./../../coinbase_keys.txt")
    transactions = getTransactionsInAllAccounts(api_key, api_secret)
    parsedTransactions = parseTransactions(transactions) #list of tuples
    # printTransactions(parsedTransactions)
    # printInFileAsJSON(parsedTransactions)
    a = parseTransactions(transactions)
    parsedTransactions.extend(a)
    # asdf = []
    # asdf.//mmmm
    add_to_pdf.add_to_pdf(parsedTransactions)



if __name__ == '__main__':
    main()