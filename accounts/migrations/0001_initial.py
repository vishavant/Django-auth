# Generated by Django 4.1.5 on 2023-01-28 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('is_trainer', models.BooleanField(default=False)),
                ('is_counsellor', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_id', models.CharField(max_length=20)),
                ('trainer_address', models.CharField(blank=True, max_length=200, null=True)),
                ('trainer_city', models.CharField(blank=True, max_length=200, null=True)),
                ('trainer_state', models.CharField(blank=True, max_length=200, null=True)),
                ('trainer_dob', models.DateField(blank=True, null=True)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='accounts/trainer_profile_pic')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=20, null=True)),
                ('student_address', models.CharField(blank=True, max_length=200, null=True)),
                ('student_city', models.CharField(blank=True, max_length=200, null=True)),
                ('student_state', models.CharField(blank=True, max_length=200, null=True)),
                ('student_dob', models.DateField(blank=True, null=True)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='accounts/student_profile_pic')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Counsellor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counsellor_id', models.CharField(blank=True, max_length=20, null=True)),
                ('counsellor_address', models.CharField(blank=True, max_length=200, null=True)),
                ('counsellor_city', models.CharField(blank=True, max_length=200, null=True)),
                ('counsellor_state', models.CharField(blank=True, max_length=200, null=True)),
                ('counsellor_dob', models.DateField(blank=True, null=True)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='accounts/counsellor_profile_pic')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
