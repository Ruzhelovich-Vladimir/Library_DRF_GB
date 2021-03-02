from rest_framework.viewsets import ModelViewSet
from .models import UserProfile

from authapp.serializers import UserProfileModelSerializer

class UserProfileModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileModelSerializer
