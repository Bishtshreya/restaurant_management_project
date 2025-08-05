from rest_framework.views import APIView
from rest_framework.response import Response

class MenuAPIView(APIView):
    def get(self, request):
        menu = [
            {"name": "Pasta", "description": "Creamy Alfredo pasta", "price": 250},
            {"name": "Burger", "description": "Beef patty with cheese", "price": 180},
            {"name": "Pizza", "description": "Margherita with fresh basil", "price": 300},
        ]
        return Response(menu)

