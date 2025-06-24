from django.urls import path
from Admin import views
app_name = 'webadmin'

urlpatterns = [

    path('home/',views.home,name="Home"),
    
    path('dep/',views.depr,name="Department"), 
    path('deldep/<int:did>',views.del_dep,name="del_dep"),
    
    path('cou/',views.cour,name="Course"),
    path('district/',views.dist,name="District"),
    path('deldis/<int:did>',views.del_dis,name="del_dis"),
    path('place/',views.plc,name="Place"),
    path('delplc/<int:pid>',views.del_plc,name="Del_Plc"),
    path('designation/',views.desg,name="Designation"),
    path('deldsg/<int:dsg>',views.del_dsg,name="del_dsg"),


    path('userverify/',views.uvef,name="UserVerification"),
    path('acceptuser/<int:auid>',views.user_accept,name="accept_user"),
    path('acceptedu/',views.accepted_user,name="AcceptedUser"),
    path('rejectuser/<int:buid>',views.user_reject,name="reject_user"),
    path('rejectedu/',views.rejected_user,name="RejectedUser"),

    path('companyverify/',views.cvef,name="CompanyVerification"),
    path('acceptcompany/<int:vuid>',views.company_accept,name="accept_company"),
    path('acceptedt/',views.accepted_company,name="AcceptedCompany"),
    path('rejectcom/<int:xuid>',views.company_reject,name="reject_company"),
    path('rejectedt/',views.rejected_company,name="RejectedCompany"),
    

]
