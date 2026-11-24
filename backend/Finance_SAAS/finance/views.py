
from rest_framework.viewsets import ModelViewSet

from finance.task import analyze_spending
from services.budget_services import check_budget
# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CategorySerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Category, Transaction


# Create your views here.

class CategoryViewSet(ModelViewSet):
    
    serializer_class=CategorySerializer
    def get_queryset(self):
         return Category.objects.filter(user=self.request.user).select_related('user')
    
class TransactionViewSet(ModelViewSet):
    
    serializer_class=TransactionSerializer
    permission_classes=[IsAuthenticated]
    # Filter &search
    # filter_backends=[DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    # filterset_fields=['category_id','type','date']
    # ordering_fields=['amount','date']
    # search_fields=['description']
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).select_related('category')
    def perform_create(self,serializer):
        transaction=serializer.save(user=self.request.user)
        analyze_spending.delay(self.request.user.id)
        warning=check_budget(
             user=self.request.user,
             category=transaction.category,
             date=transaction.date,
        )
        if warning:
            print(warning)