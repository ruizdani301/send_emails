from django.urls import path
from . import views


app_name = 'app_emails'
urlpatterns = [
   
    path("",views.EmailsView.as_view(), name="emails"),
    path("bye/",views.ThankView.as_view(), name="thank"),]