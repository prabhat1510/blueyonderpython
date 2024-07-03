from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name="customerapp"
urlpatterns = [
    path('', views.index,name="index"),
    #path("", views.IndexView.as_view(), name="index"),
    path('data/',views.getData,name="getdata"),
    path('postdata/',views.postData,name="postdata"),
    path('customers/',views.getCustomers,name="getcustomers"),
    path('addcustomer/',views.postCustomer,name="postcustomer"),
    path('customer/<int:id>/',views.getCustomerById,name="getcustomerbyid"),
    path('customer/<str:cname>/',views.getCustomerByName,name="getcustomerbyname"),
    path('customer',views.getCustomerByNameUsingReqParams,name="getCustomerByNameUsingReqParams"),
    path('deletecustomer',views.deleteCustomerById,name="deleteCustomerById"),
]