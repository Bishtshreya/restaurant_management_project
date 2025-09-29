from rest_framework.views import APIView
from rest_framework.response import response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, genrics, permissions
from rest_framework.decorators import api_view, permission_classes

from .models import Order, OrderStatus
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

        new_status = request.data.get("new_status")

        if not new_status:
            return Response({"error": "new_status is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            status_obj = OrderStatus.objects.get(name__iexact=new_status)
        except OrderStatus.DoesNotExist:
            return Response({"error": f"Invalid status '{new_status}'"}, status=status.HTTP_400_BAD_REQUEST)

        order.status = status_obj
        order.save()

        return Response(
            {"message": f"Order #{order.id} status updated to '{new_status}'."},
            status=status.HTTP_200_OK,
        )

# 4. Get Order Status (Function-Based View)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_order_status(request, order_id):
    """
    Retrieve the current status of an order by ID.
    """
    try:
        order = Order.objects.get(id=order_id, customer=request.user)
    except Order.DoesNotExist:
        return Response(
            {"error": "Order not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(
        {"order_id": order.id, "status": str(order.status)},
        status=status.HTTP_200_OK
    )