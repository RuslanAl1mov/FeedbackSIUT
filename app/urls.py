from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_home_page, name='feedback_home_page'),
    path('jajd2A86jadJF76eO4EpMCNSjak321dan2/results/', views.feedback_results_page, name='feedback_results_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
