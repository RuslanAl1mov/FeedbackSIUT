from django.shortcuts import render, get_object_or_404
from .models import *


def feedback_home_page(request):
    if request.method == "POST":
        user_language = request.POST.get('user_language')
        department_id = request.POST.get('department_id')
        subject_id = request.POST.get('subject_id')
        teacher_id = request.POST.get('teacher_id')

        teacher = get_object_or_404(Teacher, pk=teacher_id)
        subject = get_object_or_404(Subject, pk=subject_id)
        department = get_object_or_404(Department, pk=department_id)

        new_feedback = Feedback.objects.create(
            teacher=teacher,
            user_language=user_language,
            subject=subject,
            department=department
        )

        for i in range(9):
            Answer.objects.create(
                feedback=new_feedback,
                question_id=i + 1,
                answer_value=request.POST.get(f'question{i + 1}')
            )

    context = {"schools": School.objects.all()}
    return render(request, 'index.html', context=context)


def feedback_results_page(request):
    context = {'teachers': []}
    feedbacks = Feedback.objects.select_related('teacher', 'department', 'subject').all()

    existed_teachers = set()
    unique_teachers = [feedback.teacher for feedback in feedbacks if
                       feedback.teacher not in existed_teachers and not existed_teachers.add(feedback.teacher)]

    for teacher in unique_teachers:
        teacher_info = {'name': teacher, 'feedbacks': []}
        one_teacher_feedbacks = feedbacks.filter(teacher=teacher)

        existed_departments = set()
        unique_departments = [feedback.department for feedback in one_teacher_feedbacks if
                              feedback.department not in existed_departments and not existed_departments.add(
                                  feedback.department)]

        for department in unique_departments:
            department_feedbacks = {'department': department, 'subjects': [], 'feedbacks_number': 0}
            one_teacher_department_feedbacks = one_teacher_feedbacks.filter(department=department)

            existed_subjects = set()
            unique_subjects = [feedback.subject for feedback in one_teacher_department_feedbacks if
                               feedback.subject not in existed_subjects and not existed_subjects.add(feedback.subject)]

            for subject in unique_subjects:
                feedbacks_for_subject = one_teacher_department_feedbacks.filter(subject=subject)
                subject_feedbacks = {'subject': subject, 'answers': [], 'total_hor': []}

                for question_num in range(6):
                    answers = []
                    total_vert = []
                    for feedback in feedbacks_for_subject:
                        answer_obj = list(Answer.objects.filter(feedback=feedback).exclude(question_id__in=[7, 8, 9])
                                          .values('question_id', 'answer_value')
                                          .order_by('question_id'))

                        answers.append(answer_obj[question_num])
                        total_vert.append(int(answer_obj[question_num]['answer_value']))
                        if question_num == 0:
                            th = 0
                            for i in answer_obj:
                                th += int(i['answer_value'])
                            subject_feedbacks['total_hor'].append(format(th/len(answer_obj), '.2f'))
                    tv = 0
                    for i in total_vert:
                        tv += i
                    tv = tv / len(total_vert)

                    answers.append("{:.2f}".format(tv))
                    total_vert.clear()
                    subject_feedbacks['answers'].append(answers)

                th = 0
                for i in subject_feedbacks['total_hor']:
                    th += float(i)
                th = th / len(subject_feedbacks['total_hor'])
                subject_feedbacks['final_score'] = "{:.2f}".format(th)

                department_feedbacks['subjects'].append(subject_feedbacks)

            teacher_info['feedbacks'].append(department_feedbacks)

        context['teachers'].append(teacher_info)

    return render(request, 'feedback_results.html', context=context)
