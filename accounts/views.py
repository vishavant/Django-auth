from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, TrainerRegistrationForm, CousellorRegistrationForm, LoginForm
from .decorators import admin_required, student_required, trainer_required, counsellor_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import User
from django.views.generic import CreateView

# Create your views here.

# class StudenSignUpView(CreateView):
#     model = User
#     form_class = StudentRegistrationForm
#     template_name = "accounts/student_registration.html"
    

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)

def user_sign_up(request):
    return render(request, "accounts/create_users.html")


def student_signup(request):
    form_class = StudentRegistrationForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form .is_valid():
            form.save()
    else:
        return render(request, "accounts/student_registration.html", {'form':form})
    return redirect('/thanks/')
        

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


def trainer_signup(request):
    form_class = TrainerRegistrationForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form .is_valid():
            form.save()
    else:
        return render(request, "accounts/trainer_registration.html", {'form':form})
    return render(request, "accounts/thank_you.html")


def counsellor_signup(request):
    form_class = CousellorRegistrationForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        return render(request, "accounts/counsellor_signup.html", {'form':form})
    return render(request, "accounts/thank_you.html")




# def send_otp(phone, otp):
#     print(otp)
#     conn = http.client.HTTPConnection("2factor.in")
#     # authkey = settings.AUTH_KEY
#     headers = {'content-type': "application/json"}
#     conn.request("GET",
#                  "https://2factor.in/API/R1/?module=SMS_OTP&apikey=fb3df403-12c4-11eb-9fa5-0200cd936042&to=" + phone + "&otpvalue=" + str() + "&templatename=WomenMark1")
#     res = conn.getresponse()
#     data = res.read()
#     print(data)
#     return None


# # @unauthenticated_user
# def login_attempt(request):
#     if request.method == 'POST': 
#         phone = request.POST.get('phone')

#         user = User.objects.filter(phone=phone).first()

#         if user is None:
#             context = {'message': 'User not found', 'class': 'danger'}
#             return render(request, 'accounts/login.html', context)

#         otp = str(random.randint(1000, 9999))
#         user.otp = otp
#         user.save()
#         send_otp(phone, otp)
#         request.session['phone'] = phone
#         return redirect('accounts:login_otp')
#     return render(request, 'accounts/login.html')


# def login_otp(request):
#     phone = request.session['phone']
#     context = {'phone': phone}
#     if request.method == 'POST':
#         otp = request.POST.get('otp')
#         user = User.objects.filter(phone=phone).first()

#         if otp == user.otp:
#             user = User.objects.get(id=user.user.id)
#             login(request, user)
#             return redirect('reports:admin_dashboard')
#         else:
#             context = {'message': 'Wrong OTP', 'class': 'danger', 'phone': phone}
#             return render(request, 'accounts/login_otp.html', context)

#     return render(request, 'accounts/login_otp.html', context)


# def user_login(request):
#     if request.method == 'POST':    
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         print(phone)
#         print(password)

#         user = authenticate(request, phone=phone, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Logged in Successfully")
#             return redirect('accounts:stu-profile')
#         else:
#             messages.info(request, "Username or Password is incorrect")
    
#     return render(request, "accounts/login.html", )



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
            else:
                messages.info(request, 'Username OR password is incorrect')
    else:
        login_form = LoginForm()  
    return render(request, "accounts/login.html", {'form':login_form})
    

    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('user-signup/')  
    



@login_required
@student_required
def student_profile(request):
    return render(request, "accounts/student_profile.html")


@login_required
@trainer_required
def trainer_profile(request):
    return render(request, "accounts/trainer_profile.html")


@login_required
@counsellor_required
def counsellor_profile(request):
    return render(request, "accounts/counsellor_profile.html")



@login_required
@admin_required
def admin_profile(request):
    return render(request, "accounts/admin_profile.html")


def thank_you(request):
    return render(request, "accounts/thank_you.html")



def show_users(request):
    users = User.objects.all()
    context = {
        users:users
    }
    return render(request, "accounts/users.html", context)