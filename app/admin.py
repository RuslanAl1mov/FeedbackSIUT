from django.contrib import admin

from .models import *


admin.site.register(School)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Feedback)
admin.site.register(Answer)
admin.site.register(Teacher)
admin.site.register(TeacherSubject)
admin.site.register(SubjectDepartment)


