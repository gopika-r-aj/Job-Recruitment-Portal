from django.urls import path
from Company import views
app_name = 'webcompany'

urlpatterns = [
    path('chome/',views.Companyhome,name="CompanyHome"),

    path('companyprofile/',views.companyprofile,name="Companyprofile"),
    path('editcompanyprofile/',views.editcompanyprofile,name="EditCompanyProfile"),
    path('cngpassword/',views.changecompanypassword,name="ChangeCompanyPassword"),

    path('internship/',views.internship,name="Internship"),
    path('delinternship/<int:did>',views.del_intern,name="Del_Internship"),
    
    path('placements/',views.placements,name="Placements"),
    path('delplacements/<int:pid>',views.del_placent,name="Del_Placements"),

    path('viewinternshipapplications/',views.viewintapps,name="ViewInternshipApplications"),
    path('accept_internship/<int:acint>',views.accept_internship,name="accept_internship"),
    path('reject_internship/<rjint>',views.reject_internship,name="reject_internship"),
    
    path('acceptedinternshipapplications/',views.acceptedintapps,name="AcceptedInternshipApplications"),
    path('rejectedinternshipapplications/',views.rejectedintapps,name="RejectedInternshipApplications"),

    path('viewplacementapplications/',views.viewintplcs,name="ViewPlacementApplications"),
    path('accept_placement/<int:acplc>',views.accept_placement,name="accept_placement"),
    path('reject_placement/<rjplc>',views.reject_placement,name="reject_placement"),
    
    path('acceptedplacementapplications/',views.acceptedplcapps,name="AcceptedPlacementApplications"),
    path('rejectedplacementapplications/',views.rejectedplcapps,name="RejectedPlacementApplications"),
]
