from rest_framework import serializers
from student.serializers import StudentSerializer
from .models import Log

class reportCardSerializer(serializers.ModelSerializer):
    student=StudentSerializer()
    class Meta:
        model = Log
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        # depth=1