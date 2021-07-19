from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from _admin import views

app_name = 'admin'
urlpatterns = [
    path(
        'statistic/',
        views.AdminStatisticView.as_view(),
        name='statistic',
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
