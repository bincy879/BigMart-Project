from django.urls import path
from front_end import views


urlpatterns=[
    path('home/',views.home,name="home"),
    path('aboutfn/',views.aboutfn,name="aboutfn"),
    path('productsfn/',views.productsfn,name="productsfn"),
    path('disCat/<itemCatg>/',views.disCat,name="disCat"),
    path('show_pdt_detls/<int:dataid>/',views.show_pdt_detls,name="show_pdt_detls"),
    path('registr/',views.registr,name="registr"),
    path('registr_save/',views.registr_save,name="registr_save"),
    path('login/',views.login,name="login"),
    path('login_save/',views.login_save,name="login_save"),
    path('logout/',views.logout,name="logout"),
    path('contact/',views.contact,name="contact"),
    path('msgSave/',views.msgSave,name="msgSave")




]