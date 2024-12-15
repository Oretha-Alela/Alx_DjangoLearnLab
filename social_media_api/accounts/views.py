from django.shortcuts import render

# Create your views here
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from rest_framework import serializers, status

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        from django.contrib.auth import authenticate

        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    





from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if request.user == user_to_follow:
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)
    return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if request.user == user_to_unfollow:
        return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)

generics.GenericAPIView, permissions.IsAuthenticated, CustomUser.objects.all()