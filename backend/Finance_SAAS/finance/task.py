

from celery import shared_task

from finance.models import Transaction

@shared_task
def analyze_spending(user_id):
    transactions=Transaction.objects.filter(user_id=user_id)
    total=sum(t.amount for t in transactions)
    print(f"Total spending for user{user_id}:{total}")