from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from log import views as log_views
from student import views as student_views

router = routers.DefaultRouter()
router.register(r'students', student_views.StudentViewSet)
router.register(r'logs', log_views.LogViewSet)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('calc-gpa/<int:student_id>/', log_views.calc_gpa,name='calc_gpa'),
                  path('api-token-auth/', views.obtain_auth_token),
                  path('api-auth/', include('rest_framework.urls')),
              ] + router.urls
