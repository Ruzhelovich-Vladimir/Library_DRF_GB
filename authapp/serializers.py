from rest_framework.serializers import HyperlinkedModelSerializer
from .models import UserProfile

class UserProfileModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # fields = ('user_name', 'first_name', 'last_name', 'email')





