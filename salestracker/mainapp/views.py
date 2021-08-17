from django.shortcuts import render, redirect , HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import  CreateUserForm
from . models import User1
from . forms import CustomerRegistration
# Create your views here.


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'mainapp/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'mainapp/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	customers = User1.objects.all()

	return render(request, 'mainapp/dashboard.html')

#-----------------------------------------------------------------------------

@login_required(login_url='login')
def form1(request):
    if request.method=='POST':
        fm=CustomerRegistration(request.POST)
        if fm.is_valid():
            ar=fm.cleaned_data['area']
            ap=fm.cleaned_data['approch']
            ld=fm.cleaned_data['lead']
            reg=User1(area=ar, approch=ap, lead=ld)
            reg.save()
            messages.success(request, 'Congratulation !! customer added successfully')
            fm=CustomerRegistration()
            
    else:
        fm=CustomerRegistration()
    cust=User1.objects.all()
    return render(request, 'mainapp/form1.html', {'form':fm, 'stu':cust})
#------------------------------------------------------------------------------------------------
@login_required(login_url='login')
def update_data(request,id):
    if request.method=='POST':
        pi=User1.objects.get(pk=id)
        fm=CustomerRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Congratulation !! you have updated successfully')
    else:
        pi=User1.objects.get(pk=id)
        fm=CustomerRegistration(instance=pi)
    return render(request, 'mainapp/update.html', {'form':fm})



# This Function will Delete
@login_required(login_url='login')
def delete_data(request, id):
    if request.method=='POST':
        pi=User1.objects.get(pk=id)
        pi.delete()
        messages.success(request, 'You have deleted one data successfully')
        return HttpResponseRedirect('/')
#----------------------------------------------------------------------------

@login_required(login_url='login')
def form2(request):
	form2 = User1.objects.all()

	return render(request, 'mainapp/form2.html', {'form2':form2})






