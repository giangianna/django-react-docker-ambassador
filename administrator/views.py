from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.fields import REGEX_TYPE
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import ProductSerializer
from common.serializers import UserSerializer
from common.authentication import JWTAuthentication


from core.models import Product, User

# Create your views here.
class AmbassadorAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, _):
        ambassador = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassador, many=True)
        return Response(serializer.data)

class ProductGenericAPIView(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin,
    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, pk=None):
        return self.partial_update(request,pk)

    def delete(self, request, pk=None):
        return self.destroy(request,pk)