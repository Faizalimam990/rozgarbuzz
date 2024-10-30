from django.contrib import admin
from django.urls import path
from .views import home, post_job ,getjob # Explicitly importing views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),  # Home page
    path("post-job/", post_job, name="postjob"),
    path("get_job",getjob,name="getjobs")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
