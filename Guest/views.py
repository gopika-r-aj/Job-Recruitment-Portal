from django.shortcuts import render,redirect
from .models import *
from Admin.models import *


# Create your views here.


def home(request):
    return render(request,"Guest/Home.html")


def user_reg(request):
    dis=District.objects.all()
    dep=Department.objects.all()
    if request.method=="POST" and request.FILES:
        place=Place.objects.get(id=request.POST.get('sel_place'))
        course = Course.objects.get(id=request.POST.get('sel_course'))
        UserRegistration.objects.create(user_name=request.POST.get('txt_name'),
        user_contact=request.POST.get('txt_contact'),
        user_gender=request.POST.get('gender'),
        user_email=request.POST.get('txt_email'),
        user_address=request.POST.get('txt_address'),
        user_photo=request.FILES.get('txt_file'),
        user_proof=request.FILES.get('txt_proof'),
        user_password=request.POST.get('txt_password'),
        user_doj=request.POST.get('txt_doj'),
        user_graduation=request.POST.get('txt_graduation'),
        user_course=course,
        place=place),
    return render(request,"Guest/UserRegistration.html",{'DS':dis,'DEP':dep})


def ajax_plc(request):
    dist=request.GET.get('DIST')
    plc=Place.objects.filter(district=dist)
    return render(request,"Guest/AjaxPlace.html",{'PLC':plc})


def ajax_course(request):
    dept=request.GET.get('DIST')
    cou=Course.objects.filter(department=dept)
    return render(request,"Guest/AjaxCourse.html",{'COU':cou})
    


def glogin(request):
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_password')
        ulog=UserRegistration.objects.filter(user_email=Email,user_password=Password,user_vsts=1).count()
        clog=CompanyRegistration.objects.filter(company_email=Email,company_password=Password,company_vsts=1).count()
        alog=Admin.objects.filter(admin_email=Email,admin_password=Password).count()
        if ulog > 0:
            usr=UserRegistration.objects.get(user_email=Email,user_password=Password,user_vsts=1)
            request.session['uid']=usr.id
            request.session['uname']=usr.user_name
            return redirect('webuser:UserHome')
        elif clog > 0:
            cmpny=CompanyRegistration.objects.get(company_email=Email,company_password=Password,company_vsts=1)
            request.session['cid']=cmpny.id
            request.session['cname']=cmpny.company_name
            return redirect('webcompany:CompanyHome')
        elif alog > 0:
            admin=Admin.objects.get(admin_email=Email,admin_password=Password)
            request.session['aid']=admin.id
            request.session['aname']=admin.admin_name
            return redirect('webadmin:Home')
        else:
            error="Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'ER':error})
    else:
        return render(request,"Guest/Login.html")

def cmpnyreg(request):
    dis=District.objects.all()
    if request.method=="POST" and request.FILES:
        place=Place.objects.get(id=request.POST.get('sel_place'))
        CompanyRegistration.objects.create(company_name=request.POST.get('txt_name'),
            company_contact=request.POST.get('txt_contact'),
            company_email=request.POST.get('txt_email'),
            company_address=request.POST.get('txt_address'),
            company_logo=request.FILES.get('txt_logo'),
            company_proof=request.FILES.get('txt_proof'),
            company_password=request.POST.get('txt_password'),
            place=place)
        return render(request,"Guest/CompanyRegistration.html",{'DS':dis})
    else:
        return render(request,"Guest/CompanyRegistration.html",{'DS':dis})


