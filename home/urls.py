from django.contrib import admin
from django.urls import path
from .views import home, post_job  # Explicitly importing views

urlpatterns = [
    path('', home, name="home"),  # Home page
    path("post-job/", post_job, name="postjob")  # Ensure a trailing slash
]
