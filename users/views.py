from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    '''Here whenever we submit, the inputs are sent by a POST request but to the same page.
    So to differentiate between landing at the page for the first time and actually submitting a filled form, we are using the if condition. If a validated form is filled, a success message is printed using the base template from the blog app. '''
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Your account has been created. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    # We pass data to the template using a dictionary with key as var name and value as the var
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')