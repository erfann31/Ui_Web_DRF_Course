from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
