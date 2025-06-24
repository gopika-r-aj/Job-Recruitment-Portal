from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *

# Create your views here.


def home(request):
    return render(request,"Admin/Home.html")

def depr(request):
    dep=Department.objects.all()
    if request.method=="POST":
        Department.objects.create(department_name=request.POST.get('txt_deptype'))
        return render(request,"Admin/Department.html",{'DD':dep})
    else:
         return render(request,"Admin/Department.html",{'DD':dep})



def del_dep(request,did):
    Department.objects.get(id=did).delete()
    return redirect('webadmin:Department')


def cour(request):
    dep=Department.objects.all()
    cou=Course.objects.all()
    if request.method=="POST":
        dpid=request.POST.get('sel_department')
        dp=Department.objects.get(id=dpid)
        Course.objects.create(course_name=request.POST.get('txt_course'),department=dp)
        return render(request,"Admin/Course.html",{'CC':cou,'DEP':dep})
    else:
         return render(request,"Admin/Course.html",{'CC':cou,'DEP':dep})


def dist(request):
    dis=District.objects.all()
    if request.method=="POST":
        District.objects.create(district_name=request.POST.get('txt_district'))
        return render(request,"Admin/District.html",{'DS':dis})
    else:
        return render(request,"Admin/District.html",{'DS':dis})


def del_dis(request,did):
    District.objects.get(id=did).delete()
    return redirect('webadmin:District')


def plc(request):
    dis=District.objects.all()
    plc=Place.objects.all()
    if request.method=="POST":
        disid=request.POST.get('sel_district')
        dist=District.objects.get(id=disid)
        Place.objects.create(place_name=request.POST.get('txt_place'),pincode=request.POST.get('txt_pincode'),district=dist)
        return render(request,"Admin/Place.html",{'DST':dis,'PL':plc})
    else:
        return render(request,"Admin/Place.html",{'DST':dis,'PL':plc}) 


def del_plc(request,pid):
    Place.objects.get(id=pid).delete()
    return redirect('webadmin:Place')


def desg(request):
    dsg=Designation.objects.all()
    if request.method=="POST":
        Designation.objects.create(designation_name=request.POST.get('txt_designation'))
        return render(request,"Admin/Designation.html",{'DS':dsg})
    else:
        return render(request,"Admin/Designation.html",{'DS':dsg})


def del_dsg(request,dsg):
    Designation.objects.get(id=dsg).delete()
    return redirect('webadmin:Designation')


def uvef(request):
    Userverify=UserRegistration.objects.filter(user_vsts=0)
    return render(request,"Admin/UserVerification.html",{'UV':Userverify})


def user_accept(request,auid):
    uaccept=UserRegistration.objects.get(id=auid)
    uaccept.user_vsts=1
    uaccept.save()
    return redirect('webadmin:AcceptedUser')


def user_reject(request,buid):
    ureject=UserRegistration.objects.get(id=buid)
    ureject.user_vsts=2
    ureject.save()
    return redirect('webadmin:RejectedUser')

def accepted_user(request):
    usraccepted=UserRegistration.objects.filter(user_vsts=1)
    return render(request,"Admin/AcceptedUser.html",{'UV':usraccepted})


def rejected_user(request):
    usrrejected=UserRegistration.objects.filter(user_vsts=2)
    return render(request,"Admin/RejectedUser.html",{'UV':usrrejected})

def cvef(request):
    Companyverify=CompanyRegistration.objects.filter(company_vsts=0)
    return render(request,"Admin/CompanyVerification.html",{'CV':Companyverify})

def company_accept(request,vuid):
    uaccept=CompanyRegistration.objects.get(id=vuid)
    uaccept.company_vsts=1
    uaccept.save()
    return redirect('webadmin:AcceptedCompany')


def company_reject(request,xuid):
    ureject=CompanyRegistration.objects.get(id=xuid)
    ureject.company_vsts=2
    ureject.save()
    return redirect('webadmin:RejectedCompany')

def accepted_company(request):
    comaccepted=CompanyRegistration.objects.filter(company_vsts=1)
    return render(request,"Admin/AcceptedCompany.html",{'CV':comaccepted})


def rejected_company(request):
    comrejected=CompanyRegistration.objects.filter(company_vsts=2)
    return render(request,"Admin/RejectedCompany.html",{'CV':comrejected})



