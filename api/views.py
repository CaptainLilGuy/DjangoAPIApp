from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, status
from .serializers import orderSerializer, statusSerializer

@api_view(['GET'])
def show_orders(request):
    orders = Order.objects.all()
    statusTable = status.objects.all()
    ordersData = orderSerializer(orders, many=True).data
    statusData = statusSerializer(statusTable, many=True).data

    return Response({
        "data": ordersData,
        "status": statusData
    })
