from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, TrainerRegistrationForm, CousellorRegistrationForm, LoginForm
from .decorators import admin_required, student_required, trainer_required, counsellor_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import User
from django.views.generic import CreateView

# Create your views here


def user_sign_up(request):
    return render(request, "accounts/create_users.html")



class StudentSignUpView(CreateView):
    model = User
    form_class = StudentRegistrationForm
    template_name = 'accounts/student_registration.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:stu_profile')
    


class TeacherSignUpView(CreateView):
    model = User
    form_class = TrainerRegistrationForm
    template_name = 'accounts/trainer_registration.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'trainer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:tr_profile')


    
class CounsellorSignUpView(CreateView):
    model = User
    form_class = CousellorRegistrationForm
    template_name = 'accounts/counsellor_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'counsellor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:cn_profile')






def user_login(request):
    if request.method == 'POST': 
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']   
            upass = login_form.cleaned_data['password']
            user = authenticate(email=email, password=upass)
            if user is not None:
                if user.is_authenticated and user.staff:
                    login(request, user)
                    return HttpResponseRedirect('/admin_profile/')
                if user.is_authenticated and user.is_student:
                    login(request, user)
                    return HttpResponseRedirect('/stu_profile/')
                if user.is_authenticated and user.is_trainer:
                    login(request, user)
                    return HttpResponseRedirect('/tr_profile/')
                if user.is_authenticated and user.is_counsellor:
                    login(request, user)
                    return HttpResponseRedirect('/cn_profile/')
                messages.success(request, "Hii welcome back")
            else:
                messages.info(request, 'Username OR password is incorrect')
    else:
        login_form = LoginForm()  
    return render(request, "accounts/login.html", {'form':login_form})
    

    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')  
    



@login_required(login_url='accounts:login')
@student_required
def student_profile(request):
    return render(request, "accounts/student_profile.html")


@login_required(login_url='accounts:login')
@trainer_required
def trainer_profile(request):
    if not request.user.is_trainer:
        messages.error(request, "You are not allowed view this page")
        return redirect('profile', user=request.user.name)
    return render(request, "accounts/trainer_profile.html")


@login_required(login_url='accounts:login')
@counsellor_required
def counsellor_profile(request):
    return render(request, "accounts/counsellor_profile.html")



@login_required(login_url='accounts:login')
@admin_required
def admin_profile(request):
    return render(request, "accounts/admin_profile.html")


def thank_you(request):
    return render(request, "accounts/thank_you.html")


@login_required(login_url='accounts:login')
def show_users(request):
    users = User.objects.all()
    context = {
        users:users
    }
    return render(request, "accounts/users.html", context)