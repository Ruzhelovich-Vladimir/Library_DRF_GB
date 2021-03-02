from rest_framework.serializers import HyperlinkedModelSerializer
from libraryapp.models import Author

class AutorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        # fields = "__all__"
        fields = ('first_name', 'last_name', 'birthday_year')





