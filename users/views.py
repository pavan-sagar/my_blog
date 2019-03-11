from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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

@login_required #This decorator will redirect guest user to the login page if they try to access the /profile url.
def profile(request):
    
    #If user has updated details and clicked the "Update" button, we make the required changes for the user DB tables. The request.POST and request.FILES is passing the newly entered data by user.
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account has been updated.')
            return redirect('profile') #The advantage of redirecting here instead of letting the if block complete is the browser doesnt ask for form confirmation and this also prevents any duplicate rows creation in DB.
    else: #Else part means we are lading to this page using the 'Profile' link from banner and just pre-filling form with user details.
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form':u_form,'p_form':p_form}
    return render(request,'users/profile.html',context)