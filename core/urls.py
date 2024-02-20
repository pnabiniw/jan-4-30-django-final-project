from django.urls import path
from .views import HomeView, job_application, MyJobsView, JobDetailView


urlpatterns = [
    path('job-application/<int:id>/', job_application, name="job_application"),
    path('my-jobs/', MyJobsView.as_view(), name="my_jobs"),
    path('job/<int:pk>/', JobDetailView.as_view(), name="job_detail"),
    path('', HomeView.as_view(), name="home")
]
