from coinbase.wallet.client import Client


def readKeys(filename):
    file = open(filename, "r")
    lines = file.readlines()

    api_key = lines[0].strip()
    api_secret = lines[1].strip()

    return api_key, api_secret


def getTransactions(api_key, api_secret):
    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        api_version='2017-12-07')
    accounts = client.get_accounts()

    # print(len(accounts.data))
    transactions = []

    for account in accounts.data:
        # print(account.get_transactions())
        transactions.append(account.get_transactions())

    return transactions


def main():
    api_key, api_secret = readKeys("./../../coinbase_keys.txt")
    transactions = getTransactions(api_key, api_secret)
    print(len(transactions))


if __name__ == '__main__':
    main()