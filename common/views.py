from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User
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

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect Password!')
        
        return Response(UserSerializer(user).data)