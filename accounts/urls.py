from django.urls import path
from accounts import views
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('student-register', StudentSignUpView.as_view(), name='student-register'),
    path('trainer-register', TeacherSignUpView.as_view(), name='trainer-register'),
    path('counsellor-register', CounsellorSignUpView.as_view(), name='counsellor-register'),
#     path('login', views.login_view, name='login'),
#     path('thanks', views.thank_you, name='thanks'),
#     path('student-profile', views.student_profile, name='student-profile'),
#     path('trainer-profile', views.trainer_profile, name='trainer-profile'),
#     path('counsellor-profile', views.counsellor_profile, name='counsellor-profile'),
#     path('student-home', views.student_homepage, name='student-home'),
#     path('trainer-home', views.trainer_homepage, name='trainer-home'),
#     path('counsellor-home', views.counsellor_homepage, name='counsellor-home'),
    

    # path('student-registration/', views.student_signup, name='student-registration'),
    # path('trainer-registration/', views.trainer_signup, name='trainer-registration'),
    # path('counsellor-registration/', views.counsellor_signup, name='counsellor-registration'),
    path('user-signup', views.user_sign_up, name='user-signup'),
    path('login/', views.user_login, name="login"),
    path('logout', views.user_logout, name='logout'),
    path('stu_profile/', views.student_profile, name='stu_profile'),
    path('tr_profile/', views.trainer_profile, name='tr_profile'),
    path('cn_profile/', views.counsellor_profile, name='cn_profile'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('thanks/', views.thank_you, name='thanks'),
    path('show-users', views.show_users),
      ]
# ]
