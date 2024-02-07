from modeltranslation.translator import register, TranslationOptions
from .models import Department, Question, Subject, School


@register(School)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('name', 'option_1', 'option_2', 'option_3', 'option_4')
