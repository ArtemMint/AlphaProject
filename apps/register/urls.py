from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.register import views

app_name = 'register'
urlpatterns = [
    path('sign-in/',
         views.LoginUserView.as_view(),
         name='user_login',),
    path('sign-up/',
         views.RegisterUserView.as_view(),
         name='user_register',),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
