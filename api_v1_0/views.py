from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Department, Subject, Teacher, TeacherSubject, SubjectDepartment
from app.serializers import DepartmentSerializer, SubjectSerializer, TeacherSerializer


class GetDepartmentsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        school_id = request.GET.get('school_id')

        if school_id is not None:
            departments = Department.objects.filter(school_id=school_id)
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'school_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)


class GetSubjectByDepartmentIDAPIView(APIView):
    def get(self, request, *args, **kwargs):
        department_id = request.GET.get('department_id')

        if department_id is not None:
            subjects_departments = SubjectDepartment.objects.filter(department_id=department_id)
            subjects_list = []
            for sbj in subjects_departments:
                subjects_list.append(sbj.subject)
            serializer = SubjectSerializer(subjects_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'department_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)


class GetTeacherBySubjectIDAPIView(APIView):
    def get(self, request, *args, **kwargs):
        subject_id = request.GET.get('subject_id')

        if subject_id is not None:
            teachers_subjects = TeacherSubject.objects.filter(subject_id=subject_id)
            teachers_list = []
            for sbj in teachers_subjects:
                teachers_list.append(sbj.teacher)
            serializer = TeacherSerializer(teachers_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'subject_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
