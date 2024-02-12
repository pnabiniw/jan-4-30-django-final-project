from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm


def user_logout(request):
    logout(request)
    return redirect('home')


class UserLoginView(CreateView):
    template_name = "account/login.html"
    form = LoginForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={"title": "Login", "form": self.form()})

    def post(self, request, *args, **kwargs):
        form = self.form(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=un, password=pw)
            print(user)
            if not user:
                messages.error(request, "Invalid login credential")
            else:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, "Invalid login credential")
            return redirect('user_login')
