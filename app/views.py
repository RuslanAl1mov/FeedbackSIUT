from django.shortcuts import render
from .models import *


# Create your views here.


def feedback_home_page(request):
    if request.method == "POST":
        user_language = request.POST.get('user_language')
        teacher_id = request.POST.get('teacher_id')
        new_feedback = Feedback.objects.create(teacher=Teacher.objects.get(pk=teacher_id), user_language=user_language)
        for i in range(9):
            Answer.objects.create(feedback=new_feedback, question_id=i + 1,
                                  answer_value=request.POST.get(f'question{i + 1}'))

    context = {"schools": School.objects.all()}
    return render(request, 'index.html', context=context)
