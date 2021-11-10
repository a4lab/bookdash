from django.shortcuts import render

from account.forms import LoginForm, ProfileEditForm, UserEditForm, UserRegistrationForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse, response
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

from account.models import Profile
from django.contrib import messages
# Create your views here.


# def user_login(request):
#     if request.method=="POST":
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             user=authenticate(request,username=cd['username'],password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponse("Authenticated Successfully")
#                 else:
#                     return HttpResponse("Disabled account")
#             else:
#                 return HttpResponse("Invalid User")
#     else:
#         form=LoginForm()
#     return render(request, 'account/blocks/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request,"dash/dashboard.html",{'section':'dashboard'})

def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid:
            new_user=form.save(commit=False)
            # Set_password handles hashing of the user password
            
            new_user.set_password(form.cleaned_data['password'])
            
            new_user.save()
            # Create new profile
            Profile.objects.create(user=new_user)
            return render(request,"auth/register_done.html",{'new_user':new_user})
    else:
        form=UserRegistrationForm()
    return render(request,"auth/register.html",{'form':form})

@login_required
def edit(request):
    resp=None
    user = request.user
    profile = Profile.objects.get(user_id=user)  

    if request.method=="POST":
        user_form=UserEditForm(instance=request.user,data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
    
        if user_form.is_valid() and profile_form.is_valid():
            if user_form.save() and profile_form.save():
                resp="Edit Successful"
            else:
                resp="Edit Failed"
    else:
        user_form=UserEditForm(initial=model_to_dict(user))
        profile_form=ProfileEditForm(initial=model_to_dict(profile))
    return render(request,"dash/edit.html",{'userform':user_form,'profileform':profile_form,'resp':resp})