from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import Category, Job, JobApplication, Contact


class HomeView(ListView):
    template_name = 'core/home.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Job.objects.exclude(
                jobapplication__status__in=["APPLIED", "SCREENING", "SHORT_LISTED", "REJECTED", "SELECTED"],
                jobapplication__user=self.request.user
            )
        return Job.objects.all()


def job_application(request, id):
    if request.method == "POST":
        try:
            resume = request.user.userprofile.resume
        except:
            messages.error(request, "Please complete your profile!!")
            return redirect("home")
        if not resume:
            messages.error(request, "Please upload your resume to apply for a job")
            return redirect('home')
        JobApplication.objects.create(user=request.user, job_id=id, status="APPLIED")
        messages.success(request, "Successfully applied for the job !!")
    return redirect('home')


class MyJobsView(ListView):
    template_name = 'core/my_jobs.html'
    context_object_name = 'job_applications'

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)


class JobDetailView(DetailView):
    template_name = 'core/job_detail.html'
    queryset = Job.objects.all()
    context_object_name = "job"


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Contact.objects.create(name=name, subject=subject, message=message)
        messages.success(request, "Thank you. We will respond soon !!")
        return redirect("home")
    return render(request, template_name="core/contact_us.html")
