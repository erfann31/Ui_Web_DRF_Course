from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = '__all__'
    ordering_fields = ['name', 'national_code', 'created_at']
    search_fields = ['name']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
