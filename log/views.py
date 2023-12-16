from rest_framework.viewsets import ModelViewSet

from .models import Log
from .serializers import reportCardSerializer


class LogViewSet(ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = reportCardSerializer
