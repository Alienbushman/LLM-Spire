from django.conf import settings
from django.urls import path

from .views import LLMOpinionModelView, RunningDevice, DeviceUsage

urlpatterns = [
    path('llm-opinion/', LLMOpinionModelView.as_view()),
    path('running-device/', RunningDevice.as_view()),
    path('device-usage/', DeviceUsage.as_view())
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
