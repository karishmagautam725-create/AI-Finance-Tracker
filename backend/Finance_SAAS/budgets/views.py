from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from finance.models import Budget
from .serializers import BudgetSerializer

# Create your views here.
class BudgetViewSet(ModelViewSet):
    serializer_class=BudgetSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Budget.objects.select_related("category").filter(user=self.request.user)
    def perform_create(self, serializer):
         serializer.save(user=self.request.user)