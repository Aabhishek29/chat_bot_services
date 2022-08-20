# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import ChatBotSerializer
from .models import ChatModel


# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = ChatModel.objects.all()

    # specify serializer to be used
    serializer_class = ChatBotSerializer
