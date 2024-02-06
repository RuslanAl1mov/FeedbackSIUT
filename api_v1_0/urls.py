from django.urls import path
from .views import *

urlpatterns = [
    path('siut/get_departments/', GetDepartmentsAPIView.as_view(), name='get_departments_api'),
    path('siut/get_subjects_by_department_id/', GetSubjectByDepartmentIDAPIView.as_view(), name='get_subjects_by_department_id_api'),
    path('siut/get_teachers_by_subject_id/', GetTeacherBySubjectIDAPIView.as_view(),
         name='get_teachers_by_subject_id_api'),

]