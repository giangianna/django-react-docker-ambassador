from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serilizers import UserSerializer


# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confrim']:
            raise exceptions.APIException('Password do not match!')
        
        data['is_ambassador'] = 0

        serializers = UserSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
