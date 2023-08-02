from django.shortcuts import render,redirect
from .forms import*
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(r):
    data={}
    data['student']=Student.objects.all()
    data['category']=Category.objects.all()
    data['shift']=Shift.objects.all()
    return render(r,'home.html',data)


def base(r):
    return render(r,'base.html')

def add_student(r):
    form=StudentForm(r.POST or None)
    if(r.method=="POST"):
        if(form.is_valid()):
            form.save()
            return redirect(home)
        
    return render(r,'Add_Student.html',{'form':form})

def search(r):
    data={}
    data['shift']=Shift.objects.all()
    data['category']=Category.objects.all()
    data['student']=Student.objects.filter(name__icontains=r.GET.get('search'))
    if data:
        return render(r,'home.html',data)
    
    return render(r,'home.html',data)
@login_required
def deletefun(r,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect(home)
@login_required
def update(r,id):
    student=Student.objects.get(id=id)
    form=StudentForm(r.POST or None,instance=student)
    if(r.method=="POST"):
        if(form.is_valid()):
            form.save()
            return redirect(home)
    return render(r,'update.html',{'form':form})


def register(r):
    form=UserCreationForm(r.POST or None)
    if(r.method=="POST"):
        if(form.is_valid()):
            form.save()
            return redirect(loginfun)
    return render(r,'register.html',{'form':form})

def loginfun(r):
    form=AuthenticationForm(r.POST or None)
    username=r.POST.get('username')
    password=r.POST.get('password')
    user=authenticate(username=username,password=password)
    if r.method=="POST":
        if user is not None:
            login(r,user)
            return redirect(home)
        else:
             messages.error(r,'invalid  username or password!!!!!!!')

    return render(r,'login.html',{'form':form})

def logoutfun(r):
    
    logout(r)
    return redirect(home)

def filter(r,slug):
    data={}
    data['shift']=Shift.objects.all()
    data['category']=Category.objects.all()
    data['student']=Student.objects.filter(prep_for__slug=slug)
    return render(r,'home.html',data)

def shift(r,slug):
    data={}
    data['shift']=Shift.objects.all()
    data['category']=Category.objects.all()
    data['student']=Student.objects.filter(shift__slug=slug)
    return render(r,'home.html',data)

