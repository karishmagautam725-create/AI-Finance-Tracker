from rest_framework.routers import DefaultRouter

from budgets.views import BudgetViewSet
from .views import CategoryViewSet, TransactionViewSet
router=DefaultRouter()
# router.register("transactions",TransactionViewSet)
router.register("categories",CategoryViewSet,basename="categories")
router.register("transaction",TransactionViewSet,basename="transaction")
router.register("budget",BudgetViewSet,basename="budget")
urlpatterns = router.urls

