from rest_framework import serializers
from django.db.models import Sum
from finance.models import Budget, Transaction

class BudgetSerializer(serializers.ModelSerializer):
    remaining_budget=serializers.SerializerMethodField()
    class Meta:
        model=Budget
        fields=[
            "id",
            "category",
            "amount",
            "month",
            "year",
            "remaining_budget"
        ]
    def get_remaining_budget(self,obj):
        spent=Transaction.objects.filter(
            user=obj.user,
            category=obj.category,
            date__month=obj.month,
        ).aggregate(total=Sum("amount"))["total"] or 0
        return obj.amount-spent