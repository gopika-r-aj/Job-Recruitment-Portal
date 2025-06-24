from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Company.models import *
from User.models import *
# Create your views here.

def userhome(request):
    if 'uid' in request.session:
        home=UserRegistration.objects.get(id=request.session['uid'])
        return render(request,"User/UserHome.html",{'UH':home})
    else:
        return redirect('webguest:Home')


def myprofile(request):
    if 'uid' in request.session:
        usr=UserRegistration.objects.get(id=request.session['uid'])
        return render(request,"User/Myprofile.html",{'USR':usr})
    else:
        return redirect('webguest:Home')


def editprofile(request):
    if 'uid' in request.session:
        usr=UserRegistration.objects.get(id=request.session['uid'])
        if request.method=="POST":
            usr.user_name=request.POST.get('txt_name')
            usr.user_contact=request.POST.get('txt_contact')
            usr.user_email=request.POST.get('txt_email')
            usr.user_address=request.POST.get('txt_address')
            usr.save()
            return redirect('webuser:Editprofile')
        else:
            return render(request,"User/Editprofile.html",{'EP':usr})
    else:
        return redirect('webguest:Home')
    

def changepassword(request):
    if 'uid' in request.session:
        usr=UserRegistration.objects.get(id=request.session['uid'])
        if request.method=="POST":
            pwd=usr.user_password
            current=request.POST.get('txt_curpassword')
            if pwd == current:
                usr=UserRegistration.objects.get(id=request.session['uid'])
                new=request.POST.get('txt_nwpassword')
                usr.user_password=new
                usr.save()
                return redirect('webguest:Login')
            else:
                error="Incorrect Password!!"
                return render(request,"User/ChangePassword.html",{'ER':error})
        else:
            return render(request,"User/ChangePassword.html")
    else:
        return redirect('webguest:Home')
    

def viewinternships(request):
    if 'uid' in request.session:
        int=tbl_internship.objects.all()
        return render(request,"User/ViewInternships.html",{'INT':int})
    else:
        return redirect('webguest:Home')

def apply_intern(request,intid):
    if 'uid' in request.session:
        interns=tbl_internship.objects.get(id=intid)
        usr=UserRegistration.objects.get(id=request.session['uid'])
        Internship_Apply.objects.create(internship=interns,user=usr)
        return redirect('webuser:UserHome')
    else:
        return redirect('webguest:Home')   


def viewplacements(request):
    if 'uid' in request.session:
        plcmnt=tbl_placements.objects.all()
        return render(request,"User/ViewPlacements.html",{'PLCMNT':plcmnt})
    else:
        return redirect('webguest:Home')   


def apply_placent(request,plcid):
    if 'uid' in request.session:
        placent=tbl_placements.objects.get(id=plcid)
        usr=UserRegistration.objects.get(id=request.session['uid'])
        Placement_Apply.objects.create(placement=placent,user=usr)
        return redirect('webuser:UserHome')
    else:
        return redirect('webguest:Home')     
        
        
        
def intapps(request):
    if 'uid' in request.session:
        usr=UserRegistration.objects.get(id=request.session['uid'])
        intapplctns=Internship_Apply.objects.filter(user=usr)
        return render(request,"User/MyInternshipApplications.html",{'IntApplctn':intapplctns})
    else:
        return redirect('webguest:Home') 


def plcapps(request):
    if 'uid' in request.session:
        usr=UserRegistration.objects.get(id=request.session['uid'])
        plcapplctns=Placement_Apply.objects.filter(user=usr)
        return render(request,"User/MyPlacementApplications.html",{'PlcApplctn':plcapplctns})
    else:
        return redirect('webguest:Home') 


def logout(request):
    del request.session['uid']
    return redirect('webguest:Home')