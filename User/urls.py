from django.urls import path
from User import views
app_name = 'webuser'

urlpatterns = [
    path('uhome/',views.userhome,name="UserHome"),

    path('myprofile/',views.myprofile,name="Myprofile"),
    path('editprofile/',views.editprofile,name="Editprofile"),
    path('cngpassword/',views.changepassword,name="ChangePassword"),

    path('vewinterns/',views.viewinternships,name="ViewInternships"),
    path('applyintern/<int:intid>',views.apply_intern,name="apply_internship"),

    path('vewplcmnts/',views.viewplacements,name="ViewPlacements"),
    path('applyplacent/<int:plcid>',views.apply_placent,name="apply_placement"),
    
    path('internshipapplications/',views.intapps,name="InternshipApplications"),
    path('placementapplications/',views.plcapps,name="PlacementApplications"),

    path('logout/',views.logout,name="logout"),
]