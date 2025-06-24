from django.urls import path
from Guest import views
app_name = 'webguest'

urlpatterns = [
    path('userreg/',views.user_reg,name="UserReg"),  
    path('ajaxplc/',views.ajax_plc,name="Ajax_Place"),
    path('ajaxcourse/',views.ajax_course,name="Ajax_Course"),
    path('loginpage/',views.glogin,name="Login"),
    path('compnyreg/',views.cmpnyreg,name="CmpnyReg"), 
    
    path('',views.home,name="Home"), 


]