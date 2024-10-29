from django.contrib import admin
from django.urls import path
from .views import home, post_job ,getjob # Explicitly importing views

urlpatterns = [
    path('', home, name="home"),  # Home page
    path("post-job/", post_job, name="postjob"),
    path("get_job",getjob,name="getjobs")
]
