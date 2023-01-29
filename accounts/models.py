from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_active=True, is_admin=False):
        if not email:
            raise ValueError('users must have a email number')
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(
            email=email
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,

        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,

        )
        return user

# class user_type(models.Model):
#     is_teacher = models.BooleanField(default=True)
#     is_counsellor = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)    

#     def __str__(self):
#         if self.is_student == True:
#             return User.get_email(self.user) + " - is_student"
#         else:
#             return User.get_email(self.user) + " - is_teacher"

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    is_trainer = models.BooleanField(default=False)
    is_counsellor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    def get_email(self):
        return self.email

    def __str__(self):
        return f"{self.name}-{self.email}"

    def get_full_name(self):
        if self.name:
            return self.name
        else:
            return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    


class Student(models.Model):
    student_id = models.CharField(max_length=20, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_address = models.CharField(max_length=200, blank=True, null=True)
    student_city = models.CharField(max_length=200, blank=True, null=True)
    student_state = models.CharField(max_length=200, blank=True, null=True)
    student_dob = models.DateField(blank=True, null=True)
    profile_pic = models.FileField(blank=True, upload_to='accounts/student_profile_pic', null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.name}"




class Trainer(models.Model):
    trainer_id = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    trainer_address = models.CharField(max_length=200, blank=True, null=True)
    trainer_city = models.CharField(max_length=200, blank=True, null=True)
    trainer_state = models.CharField(max_length=200, blank=True, null=True)
    trainer_dob = models.DateField(blank=True, null=True)
    profile_pic = models.FileField(blank=True, upload_to='accounts/trainer_profile_pic', null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name}"


    
class Counsellor(models.Model):
    counsellor_id = models.CharField(max_length=20, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    counsellor_address = models.CharField(max_length=200, blank=True, null=True)
    counsellor_city = models.CharField(max_length=200, blank=True, null=True)
    counsellor_state = models.CharField(max_length=200, blank=True, null=True)
    counsellor_dob = models.DateField(blank=True, null=True)
    profile_pic = models.FileField(blank=True, upload_to='accounts/counsellor_profile_pic', null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.name}"