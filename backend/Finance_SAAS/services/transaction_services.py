from finance.models import Transaction


def create_transaction(user,category,amount,date,description):
    transaction=Transaction.objects.create(
        user=user,
        category=category,
        amount=amount,
        date=date,
        description=description
    )
    return transaction