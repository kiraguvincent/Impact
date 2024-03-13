from django.shortcuts import render,redirect
from Impact_app.models import  Users


# Create your views here.
def home(request):
    return render(request , 'index.html')

def register(request):
    if request.method == 'POST':
        user = Users(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        user.save()
        return redirect('/login')
    else:
        return  render(request,'register.html')

def login(request):
    return render(request,'login.html')


def adminhome(request):
    if request.method == 'POST':
        if Users.objects.filter(username=request.POST['username'],
                                password=request.POST['password']).exists():
            user = Users.objects.get(username=request.POST['username'],
                                password=request.POST['password'])
            return render(request,'adminhome.html',{'user' : user})
        else:
            return  render(request,'login.html')
    else:
        return render(request,'login.html')