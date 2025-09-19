from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from .serialize import RegisterSerialize, CustomTokenObtainPairSerializer, ChangePasswordSerialize, ProfileSelialize
from django.shortcuts import get_object_or_404
from ...models import ProfileUserX
from mail_templated import send_mail, EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
from social import settings
#from django.core.mail import EmailMessage
from rest_framework_simplejwt.exceptions import AuthenticationFailed
import jwt


User = get_user_model()

class TestEmail(APIView):
  def get(self, request, *args, **kwargs):
    self.email = 'ahmadimehrshad38380@gmail.com'
    user_obj = get_object_or_404(User, username=self.email)
    token = self.get_tokens_for_user(user_obj)
    send_mail('email/hello.tpl', {'token': token},'ahmadimehrshad38380@gmail.com' , ['ahmadimehrshad38380@gmail.com'])
    return Response('end mile')
    
  def get_tokens_for_user(self, user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token)
    }


class RegisterApiView(generics.GenericAPIView):
  serializer_class = RegisterSerialize
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data = request.data)
    if serializer.is_valid():
      print('\n', 'MEHRSHAD', '\n')
      email_obj = serializer.validated_data['username']
      serializer.save()
      data = {
        'username': email_obj
      }
      user_obj = get_object_or_404(User, username=email_obj)
      token = self.get_tokens_for_user(user_obj)
      print('\n', token, "\n")
      send_mail('email/hello.tpl', {'token': token},'ahmadimehrshad38380@gmail.com' , ['ahmadimehrshad38380@gmail.com'])
      return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=400)
    
    
  def get_tokens_for_user(self, user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token)
    }


class Logout(APIView):
    def post(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
        
        
class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer
  

class ChangePasswordView(generics.GenericAPIView):
  model = User
  serializer_class = ChangePasswordSerialize
  permission_classes = [IsAuthenticated]
  
  def get_object(self, queryset=None):
    obj = self.request.user
    return obj
    
  def put(self, request, *args, **kwargs):
    obj = request.user
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      if not obj.check_password(serializer.data.get('old_password')):
        return Response({'error': 'new_password no '}, status=400)
      obj.set_password(serializer.data.get('new_password'))
      obj.save()
      return Response("پسورد شما با موفقیت تغییر کرد", status=200)
    return Response(serializer.errors)
        
    
class ProfileApiView(generics.GenericAPIView):
  queryset = ProfileUserX.objects.all()
  serializer_class = ProfileSelialize
  permission_classes = [IsAuthenticated]
  
  def get(self, request):
    user = ProfileUserX.objects.get(user = request.user)
    serializer = ProfileSelialize(user)
    return Response(serializer.data)
    
  def put(self, request):
    user = ProfileUserX.objects.get(user = request.user)
    serializer = ProfileSelialize(user, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  
class VerifiredApiUserView(APIView):
  def post(self, request, token, *args, **kwargs):
    try:
      token_obj = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
      return Response('Your token signature has expired.')
    except jwt.DecodeError:
      return Response('token is not valid.')
    print(token_obj)
    user_obj = User.objects.get(id=token_obj.get('user_id'))
    if user_obj.is_verified:
      return Response({'detail':'Your account has been activated.'}, status=400)
    user_obj.is_verified = True
    user_obj.save()
    return Response('okey')