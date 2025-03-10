from rest_framework import viewsets
from .models import MyTable
from .serializers import MyTableSerializer

class MyTableViewSet(viewsets.ModelViewSet):
    queryset = MyTable.objects.all()
    serializer_class = MyTableSerializer
