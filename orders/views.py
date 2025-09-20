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

class OrderCancelView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, order_id):
        try:
            # Check if the order exists and belongs to the logged-in user
            order = order.objects.get(id=order_id, customer=request.user)

            # Check if the order is already cancelled or completed
            if order.status in [Order.CANCELLED, Order.COMPLETED]:
                return Response(
                    {"error": "Order cannot be cancelled. It is already completed or cancelled."},
                    status=status.HTTP_400_BAD_REQUEST,
                    )

                    # Update the order status to 'Cancelled'
            order.status = Order.CANCELLEDorder.save()

            return Response(
                {"message": "Order successfully cancelled."},
                status=status.htTp_200_OK,
            )
        except Order.DoesNotexist:
            return Response(
                {"error": "Order not found."},
                status=status.HTTP_404_NOT_FOUND,
                )
        except Exception as e:
            return Response(
            {"error": "An error occurred while processing your request.", "details": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
                            