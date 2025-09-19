from rest_framework.views import APIView
from rest_framework.response import response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, genrics, permissions

from .models import Order
from .serializers import OrderSerializer


class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            orders = Order.objects.filter(customer=request.user).order_by("-created_at")
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": "Unable to fetch order history", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return orders for the logged-in user
        return Order.objects.filter(customer=self.request.user)