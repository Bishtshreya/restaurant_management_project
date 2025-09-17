from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Item
from .serializers import ItemSerializer
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.permissions import IsAdminUser

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # Restrict update to admin users only
    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy", "create"]:
            return [IsAdminUser()]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

# API to filter menu items by category
class MenuByCategoryAPIView(APIView):
    def get(self, request):
        category_name = request.query_params.get("category", None)
        queryset = Menu.objects.all()

        if category_name:
            queryset = queryset.filter(category__name__iexact=category_name)

            serializer = MenuSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
