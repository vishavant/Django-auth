from django.contrib.auth import REDIRECT_FIELD_NAME

from django.contrib.auth.decorators import user_passes_test

def student_required(function=None, redirect_field=REDIRECT_FIELD_NAME, login_url='accounts:login'):
    '''
    Decorator to check user type
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_student,
        login_url=login_url,
        redirect_field_name=redirect_field
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def trainer_required(function=None, redirect_field=REDIRECT_FIELD_NAME, login_url='/accounts:login/'):
    """
    This decorators checks wether the user is_trainer
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_trainer,
        login_url=login_url,
        redirect_field_name=redirect_field
    )
    if function:
        return actual_decorator(function)
    return actual_decorator



def counsellor_required(function=None, redirect_field=REDIRECT_FIELD_NAME, login_url='accounts:login'):
    """
    This decorators checks wether the user is_trainer
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_counsellor,
        login_url=login_url,
        redirect_field_name=redirect_field
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def admin_required(function=None, redirect_field=REDIRECT_FIELD_NAME, login_url='accounts:login'):
    """
    This decorators checks wether the user is_trainer
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.admin,
        login_url=login_url,
        redirect_field_name=redirect_field
    )
    if function:
        return actual_decorator(function)
    return actual_decorator