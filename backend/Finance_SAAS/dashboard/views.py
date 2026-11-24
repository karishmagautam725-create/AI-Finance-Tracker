
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

from services.dashboard_services import get_dashboard_data
# Create your views here.
class DashboardView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=get_dashboard_data(request.user)
        return Response(data)