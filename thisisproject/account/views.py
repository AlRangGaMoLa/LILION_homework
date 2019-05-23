from django.shortcuts import render
from django.conttrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            user = User.objects.create_user(username=request.POST['Username'],password=request.POST['password1'])
            auth.login(request,user)
            return redirect('/login/')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password1']
        user = auth.authenticate(request, username=Username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home/')
        else:
            return render(request, 'login.html',{'error': 'username or password is incorrect'})
    else:
        return render(request,'login.html')
# Create your views here.
