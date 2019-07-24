from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth



# Create your views here.

def register(request):

    if request.method == 'POST':
        last_name = request.POST['Last_name']
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
            elif User.objects.filter(email=email).exists():
                print('email exists')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User Created')
        else:
            print('password doesnt match')

        return redirect('/')


    else:
        return render(request,'accounts/register.html')
