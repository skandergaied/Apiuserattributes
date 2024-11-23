# accounts/views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer,GroupSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .models import UserAttribute,UserGroup




class TaskViewSet(APIView):
    def get_queryset(self):
        return UserGroup.objects.all()

    def get(self, request):
        groups = self.get_queryset()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully',
                'username': user.username,
                'groups': list(user.groups.values_list('name', flat=True))
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)