from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from common.serilizers import UserSerializer

from core.models import User

# Create your views here.
class AmbassadorAPIView(APIView):
    def get(self, _):
        ambassador = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassador, many=True)
        return Response(serializer.data)