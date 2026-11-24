from finance.models import Transaction
from django.db.models import Sum
from django.db.models.functions import TruncMonth

def get_dashboard_data(user):
        income=Transaction.objects.filter(
            user=user,
            category__type="income"
        ).aggregate(total=Sum("amount"))["total"] or 0
        expense=Transaction.objects.filter(
            user=user,
            category__type="expense"
        ).aggregate(total=Sum("amount"))["total"] or 0
        balance=income-expense
        category_expense=Transaction.objects.filter(
            user=user,
            category__type="expense"
        ).values("category__name").annotate(total=Sum("amount"))

        monthly_expenses=Transaction.objects.filter(
            user=user,
            category__type="expense"
        ).annotate(
            month=TruncMonth("date")
        ).values(
            "month"
        ).annotate(
            total=Sum("amount")
        ).order_by("month")
        return {
            "total_income":float(income),
            "total_expense":float(expense),
            "balance":float(balance),
            "category_expenses":list(category_expense),
            "monthly_expenses":list(monthly_expenses)
        }

    