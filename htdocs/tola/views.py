from django.shortcuts import render
from .forms import FeedbackForm, RegistrationForm
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth


def contact(request):
    """
    Feedback form
    """
    form = FeedbackForm(initial={'submitter': request.user})

    if request.method == 'POST':
        form = FeedbackForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            messages.error(request, 'Thank you', fail_silently=False)
        else:
            messages.error(request, 'Invalid', fail_silently=False)
            print form.errors

    return render(request, "contact.html", {'form': form, 'helper': FeedbackForm.helper})


def faq(request):
    return render(request, 'faq.html')

def documentation(request):
    return render(request, 'documentation.html')


"""
Register a new User profile using built in Django Users Model
"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

"""
Update a User profile using built in Django Users Model
"""
def profile(request):
    temp_post = request.POST.copy()
    temp_post['last_login'] = request.user.last_login
    temp_post['is_active'] = request.user.is_active
    temp_post['is_superuser'] = request.user.is_superuser
    temp_post['last_login'] = request.user.last_login
    temp_post['is_staff'] = request.user.is_staff
    temp_post['date_joined'] = request.user.date_joined

    if request.method == 'POST':
        form = RegistrationForm(temp_post, instance=request.user)

        if form.is_valid():
            form.save()
            messages.error(request, 'Your profile has been updated.', fail_silently=False)
        else:
            messages.error(request, 'Invalid', fail_silently=False)
            print form.errors
    else:
        form = RegistrationForm(instance=request.user)
    return render(request, "registration/profile.html", {
        'form': form, 'helper': RegistrationForm.helper
    })

"""
Logout a user
"""
def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")

"""
Log in a user
"""
def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")