from django.contrib import admin
from django.utils.html import format_html

from .models import *


class SchoolAdmin(admin.ModelAdmin):
    model = School
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name', )
    ordering = ('name',)


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('name', 'school')
    list_filter = ('name', 'school')
    search_fields = ('name', 'school')
    ordering = ('name', 'school')


class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ('name', 'year', 'semester')
    list_filter = ('name',)
    search_fields = ('name', )
    ordering = ('name',)


class SubjectDepartmentAdmin(admin.ModelAdmin):
    model = SubjectDepartment
    list_display = ('subject', 'department')
    list_filter = ('subject', 'department')
    search_fields = ('subject', 'department')
    ordering = ('subject', 'department')


class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = ('name', 'photo')
    list_filter = ('name',)
    search_fields = ('name', )
    ordering = ('name',)

    # def thumbnail(self, obj):
    #     if obj.photo:
    #         return format_html('<img src="{}" style="width: 100px; height:100px;" />'.format(obj.photo.url))
    #     else:
    #         return '(No image)'
    #
    # thumbnail.short_description = 'Thumbnail'


class TeacherSubjectAdmin(admin.ModelAdmin):
    model = TeacherSubject
    list_display = ('teacher', 'subject')
    list_filter = ('teacher', 'subject')
    search_fields = ('teacher', 'subject')
    ordering = ('teacher', 'subject')


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'keywords')


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ('id', 'department', 'teacher', 'subject', 'user_language', 'created_at')
    list_filter = ('id', 'department', 'teacher', 'subject', 'created_at')
    search_fields = ('department', 'teacher', 'subject')
    ordering = ('id', 'department', 'teacher', 'subject', 'created_at')


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ('answer_value', 'feedback', 'question_id')
    list_filter = ('answer_value', 'feedback', 'question_id')
    search_fields = ('answer_value', 'feedback')
    ordering = ('answer_value', 'feedback', 'question_id')


admin.site.register(School, SchoolAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectDepartment, SubjectDepartmentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubject, TeacherSubjectAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Answer, AnswerAdmin)
