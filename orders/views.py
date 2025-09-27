from rest_framework.views import APIView
from rest_framework.response import response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, genrics, permissions

from .models import Order
from .serializers import OrderSerializer, OrderDetailSerializer, OrderStatusUpdateSerializer


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

# 3. Update Order Status
class UpdateOrderStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, customer=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderStatusUpdateSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Order status updated successfully", "order": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)