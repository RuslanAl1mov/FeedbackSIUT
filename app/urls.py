from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_home_page, name='feedback_home_page'),
    path('jajd2A86jadJF76eO4EpMCNSjak321dan2/results/', views.feedback_results_page, name='feedback_results_page'),
    path('jajd2A86jadJF76eO4EpMCNSjak321dan2/download_report/<int:teacher_id>/', views.download_person_feedback_report,
         name='download_person_feedback_report'),
    path('jajd2A86jadJF76eO4EpMCNSjak321dan2/full_report/', views.download_feedback_complex_results,
         name='download_feedback_complex_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
