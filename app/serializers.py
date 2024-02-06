from rest_framework import serializers
from .models import Department, Subject, Teacher, TeacherSubject


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['pk', 'name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['pk', 'department', 'subject_year', 'subject_semester', 'subject_name']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['pk', 'name', 'photo']


class TeacherSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubject
        fields = ['pk', 'teacher', 'subject']
