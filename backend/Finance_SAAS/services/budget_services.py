from finance.models import Budget, Transaction
from django.db.models import Sum

def check_budget(user,category,date):
    try:
        budget=Budget.objects.get(user=user,category=category,month=date.month)
    except Budget.DoesNotExist:
        return None
    
    spent=Transaction.objects.filter(user=user,category=category,date__month=date.month).aggregate(total=Sum("amount"))["total"] or 0
    if spent >= budget.amount:
        return "Budget Limit Exceed"
    if spent >= budget.amount*0.8:
        return "Warning:80 % budget is used"
    return None