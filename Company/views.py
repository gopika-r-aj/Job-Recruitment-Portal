from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from Admin.models import *
from Guest.models import *
from Company.models import *
from User.models import *
# Create your views here.

def Companyhome(request):
    if 'cid' in request.session:
        home=CompanyRegistration.objects.get(id=request.session['cid'])
        return render(request,"Company/CompanyHome.html",{'UH':home})
    else:
        return redirect('webguest:Home')


def companyprofile(request):
    if 'cid' in request.session:
        usr=CompanyRegistration.objects.get(id=request.session['cid'])
        return render(request,"Company/CompanyProfile.html",{'USR':usr})
    else:
        return redirect('webguest:Home')


def editcompanyprofile(request):
    if 'cid' in request.session:
        usr=CompanyRegistration.objects.get(id=request.session['cid'])
        if request.method=="POST":
            usr.company_name=request.POST.get('txt_name')
            usr.company_contact=request.POST.get('txt_contact')
            usr.company_email=request.POST.get('txt_email')
            usr.company_address=request.POST.get('txt_address')
            usr.save()
            return redirect('webcompany:EditCompanyProfile')
        else:
            return render(request,"Company/EditCompanyProfile.html",{'EP':usr})
    else:
        return redirect('webguest:Home')
    

def changecompanypassword(request):
    if 'cid' in request.session:
        usr=CompanyRegistration.objects.get(id=request.session['cid'])
        if request.method=="POST":
            pwd=usr.company_password
            current=request.POST.get('txt_curpassword')
            if pwd == current:
                usr=CompanyRegistration.objects.get(id=request.session['cid'])
                new=request.POST.get('txt_nwpassword')
                usr.company_password=new
                usr.save()
                return redirect('webguest:Login')
            else:
                error="Incorrect Password!!"
                return render(request,"Company/ChangeCompanyPassword.html",{'ER':error})
        else:
            return render(request,"Company/ChangeCompanyPassword.html")
    else:
        return redirect('webguest:Home')
    

def internship(request):
    if 'cid' in request.session:
        cmpny=CompanyRegistration.objects.get(id=request.session['cid'])
        intern=tbl_internship.objects.all()
        if request.method=="POST":
            tbl_internship.objects.create(int_title=request.POST.get('txt_title'),int_post=request.POST.get('txt_post'),
                int_date=request.POST.get('txt_date'),int_duration=request.POST.get('txt_duration'),int_details=request.POST.get('txt_details'),
                int_stipend=request.POST.get('txt_stipend'),company=cmpny)
            return render(request,"Company/Internship.html",{'INT':intern})
        else:
            return render(request,"Company/Internship.html",{'INT':intern})
    else:
        return redirect('webguest:Home')

def del_intern(request,did):
    if 'cid' in request.session:
        tbl_internship.objects.get(id=did).delete()
        return redirect('webcompany:Internship')
    else:
        return redirect('webguest:Home')

def placements(request):
    if 'cid' in request.session:
        cmpny=CompanyRegistration.objects.get(id=request.session['cid'])
        dsgntn=Designation.objects.all()
        placent=tbl_placements.objects.all()
        if request.method=="POST":
            dsgnid=request.POST.get('sel_designation')
            dsgn=Designation.objects.get(id=dsgnid)
            tbl_placements.objects.create(plc_title=request.POST.get('txt_title'),plc_designation=dsgn,
                plc_date=request.POST.get('txt_date'),plc_salary=request.POST.get('txt_salary'),plc_details=request.POST.get('txt_details'),company=cmpny)
            return render(request,"Company/Placements.html",{'PLC':placent,'DSGN':dsgntn})
        else:
            return render(request,"Company/Placements.html",{'PLC':placent,'DSGN':dsgntn})
    else:
        return redirect('webguest:Home')

def del_placent(request,pid):
    if 'cid' in request.session:
        tbl_placements.objects.get(id=pid).delete()
        return redirect('webcompany:Placements')
    else:
        return redirect('webguest:Home')


def viewintapps(request):
    if 'cid' in request.session:
        cmpny=CompanyRegistration.objects.get(id=request.session['cid'])
        intapplctns=Internship_Apply.objects.filter(internship__company=cmpny,intapply_sts=0)
        return render(request,"Company/ViewInternshipApplications.html",{'IntApplctn':intapplctns})
    else:
        return redirect('webguest:Home')


def accept_internship(request,acint):
    if 'cid' in request.session:
        accint=Internship_Apply.objects.get(id=acint)
        accint.intapply_sts=1
        name=accint.user.user_name
        email=accint.user.user_email
        name1=accint.internship.company.company_name
        send_mail(
                'Respected sir/madam '+name, #subject
                "\rYour Internship Application is Successfully Confirmed By  " + name1 + " and we are happy to welcome you to do Internship at " + name1 + ".\n Thank you for choosing us. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we are always happy to help!. \r\n \r\n Team Graspit.\n Thank you.",#body
                settings.EMAIL_HOST_USER,
                [email],

            )
        accint.save()
        return redirect('webcompany:AcceptedInternshipApplications')
    else:
        return redirect('webguest:Home')



def reject_internship(request,rjint):
    if 'cid' in request.session:
        rjctint=Internship_Apply.objects.get(id=rjint)
        rjctint.intapply_sts=2
        name=rjctint.user.user_name
        email=rjctint.user.user_email
        name1=rjctint.internship.company.company_name
        send_mail(
                'Respected sir/madam '+name, #subject
                "\rWe thank you for applying for an internship at  " + name1 + ". Regrettably, we only require one intern, and we received a large volume of applications. After a vigorous selection process, we're writing to inform you that your application for an internship was unsuccessful. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Graspit.\n Thank you.",#body
                settings.EMAIL_HOST_USER,
                [email],

            )
        rjctint.save()
        return redirect('webcompany:RejectedInternshipApplications')
    else:
        return redirect('webguest:Home')

def acceptedintapps(request):
    if 'cid' in request.session:
        cmpny=CompanyRegistration.objects.get(id=request.session['cid'])
        intapplctns=Internship_Apply.objects.filter(internship__company=cmpny,intapply_sts=1)
        return render(request,"Company/AcceptedInternship.html",{'IntApplctn':intapplctns})
    else:
        return redirect('webguest:Home')


def rejectedintapps(request):
    if 'cid' in request.session:
        cmpny=CompanyRegistration.objects.get(id=request.session['cid'])
        intapplctns=Internship_Apply.objects.filter(internship__company=cmpny,intapply_sts=2)
        return render(request,"Company/RejectedInternship.html",{'IntApplctn':intapplctns})
    else:
        return redirect('webguest:Home')

def viewintplcs(request):
    if 'cid' in request.session:
        cmpny=CompanyRegistration.objects.get(id=request.session['cid'])
        plcapplctns=Placement_Apply.objects.filter(placement__company=cmpny,plcapply_sts=0)
        return render(request,"Company/ViewPlacementApplications.html",{'PlcApplctn':plcapplctns})
    else:
        return redirect('webguest:Home')

def accept_placement(request,acplc):
    if 'cid' in request.session:
        acplc=Placement_Apply.objects.get(id=acplc)
        acplc.plcapply_sts=1
        name=acplc.user.user_name
        email=acplc.user.user_email
        name1=acplc.placement.company.company_name    
        desig=acplc.placement.plc_designation 
        send_mail(
                'Respected sir/madam '+name, #subject
                "\rYour Placement Application is Successfully Confirmed By  " + name1 + ". We were all very excited to meet and get to know you over the past few days. We have been impressed with your background and would like to formally offer you the position of  " + desig + ".\n Thank you for choosing us. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we are always happy to help!. \r\n \r\n Team Graspit.\n Thank you.",#body
                settings.EMAIL_HOST_USER,
                [email],

            )
        acplc.save()
        return redirect('webcompany:AcceptedPlacementApplications')
    else:
        return redirect('webguest:Home')


def reject_placement(request,rjplc):
    if 'cid' in request.session:
        rjctplc=Placement_Apply.objects.get(id=rjplc)
        rjctplc.plcapply_sts=2
        name=rjctplc.user.user_name
        email=rjctplc.user.user_email
        name1=rjctplc.placement.company.company_name
        desig=rjctplc.placement.plc_designation 
        send_mail(
                'Respected sir/madam '+name, #subject
                "\rThis is from " + name1 + ".We Thank you taking the time and interviewing with us for the  " + desig + " position. Although your experience and qualifications are impressive, we are sorry to apprise you that another candidate has been selected, who feel is more suitable for the job. \n We appreciate your interest in our company. Please feel free to connect us for future openings. \r\n If you have any questions and if there is anything we can improve please reply to this email. \r\n we were always happy to help!. \r\n \r\n Team Graspit.\n Thank you.",#body
                settings.EMAIL_HOST_USER,
                [email],

            )
        rjctplc.save()
        return redirect('webcompany:RejectedPlacementApplications')
    else:
        return redirect('webguest:Home')



def acceptedplcapps(request):
    if 'cid' in request.session:
        cmpny=CompanyRegistration.objects.get(id=request.session['cid'])
        plcapplctns=Placement_Apply.objects.filter(placement__company=cmpny,plcapply_sts=1)
        return render(request,"Company/AcceptedPlacements.html",{'PlcApplctn':plcapplctns})
    else:
        return redirect('webguest:Home')



def rejectedplcapps(request):
    if 'cid' in request.session:
        cmpny=CompanyRegistration.objects.get(id=request.session['cid'])
        plcapplctns=Placement_Apply.objects.filter(placement__company=cmpny,plcapply_sts=2)
        return render(request,"Company/RejectedPlacements.html",{'PlcApplctn':plcapplctns})
    else:
        return redirect('webguest:Home')
