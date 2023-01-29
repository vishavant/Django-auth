from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin

User = get_user_model()

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Student, Trainer, Counsellor
from .forms import UserAdminCreationForm, UserAdminChangeForm

# from .models import Profile, emailOTP

# admin.site.register(emailOTP)


# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'email', 'mobile', 'staff','admin', 'is_student', 'is_trainer', 'is_counsellor')
    list_filter = ( 'staff', 'active', 'admin',)
    fieldsets = (
        # (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'mobile', 'email', 'password',)}),
        ('User Types', {'fields': ('is_student', 'is_trainer', 'is_counsellor' )}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )

    search_fields = ('email', 'name')
    ordering = ('email', 'name')
    filter_horizontal = ()



    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, UserAdmin,)
admin.site.register(Trainer)
admin.site.register(Student)


admin.site.register(Counsellor)


# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)