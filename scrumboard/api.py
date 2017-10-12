from rest_framework.generics import ListAPIView

from .serializers import *
from .models import *

class ListApi(ListAPIView):

    queryset = List.objects.all()
    serializer_class = ListSerializer

class CardApi(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

