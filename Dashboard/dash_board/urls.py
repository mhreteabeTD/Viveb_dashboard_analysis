# In your dashboard/urls.py file

from django.urls import path


from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('dashboard/', views.main_dashboard, name='dashboard'),
    path('',views.home_page,name="homepage"),
     path('upload/', views.file_upload, name='file_upload')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)