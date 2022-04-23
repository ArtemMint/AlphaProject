from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.website import views

app_name = 'website'
urlpatterns = [
    path('',
         views.HomeView.as_view(),
         name='home_page',),
    path('about',
         views.AboutView.as_view(),
         name='about_page',),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
