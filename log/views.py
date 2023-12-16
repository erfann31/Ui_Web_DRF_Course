from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from student.models import Student
from .models import Log
from .serializers import reportCardSerializer


class LogViewSet(ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = reportCardSerializer


@api_view(['GET'])
def calc_gpa(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
        log = Log.objects.filter(student=student)
        curses = 0
        total = 0

        for log in log:
            curses = 4
            total += (log.math + log.physic + log.chemistry + log.farsi)

        if curses == 0:
            return Response({'detail': 'no log for this student'}, status=status.HTTP_404_NOT_FOUND)

        gpa = total / curses
        return Response({'student_id': student_id, 'gpa': gpa}, status=status.HTTP_201_CREATED)
    except Student.DoesNotExist:
        return Response({"detail": "Student doesnt exist"}, status=status.HTTP_404_NOT_FOUND)
