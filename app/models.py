from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    year = models.IntegerField(null=False, blank=False, default=1)
    semester = models.IntegerField(null=False, blank=False, default=1)
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class SubjectDepartment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)


class Teacher(models.Model):
    name = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='teachers/img/', null=False, blank=False, default='teachers/img/user.png')

    def __str__(self):
        return self.name


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)


class Question(models.Model):
    name = models.CharField(max_length=1000)
    option_1 = models.CharField(max_length=500)
    option_2 = models.CharField(max_length=500)
    option_3 = models.CharField(max_length=500)
    option_4 = models.CharField(max_length=500)


class Feedback(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True,)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    user_language = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, null=True, blank=True)
    question_id = models.IntegerField(null=False, blank=False)
    answer_value = models.CharField(max_length=1000, blank=True, null=False, default="")
