from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@csrf_exempt
def login(request):
    if request.method == 'POST':
        number = request.POST['number']
        password = request.POST['password']
        
        user = authenticate(request , username=number , password=password)
        if user is not None:
                auth_login(request,user)
                messages.success(request, "LOgin hogya hai ")
                return redirect('/home/')
        else:
            messages.error(request , "something went wrong")
            return redirect('/login')
    return render(request , 'login.html')



def register(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname'] 
        number = request.POST['number']
        email = request.POST['email'] 
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if len(number) != 10:
            messages.error(request,'Number Should Be 10 Digit')
            return redirect('/')

        elif password != cpassword:
            messages.error(request , "Password & confirm password match nahi hue hai waps dekho achese!!!!")
            return redirect('/')
        
        else:
            user = User.objects.create( username=number,email=email , password=cpassword)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request , f'Lo bhai {fname} ban gya Account apka [AATE REHENA]')
            return redirect('/login')
    return render(request , 'register.html')


def home(request):
    return render(request , 'home.html')
