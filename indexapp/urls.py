from django.urls import path
from indexapp import views

urlpatterns=[
    path('index_fn/',views.index_fn,name="index_fn"),
    path('add_data/',views.add_data,name="add_data"),
    path('save_data/',views.save_data,name="save_data"),
    path('display_admin/',views.display_admin,name="display_admin"),
    path('edit_data/<int:dataid>/',views.edit_data,name="edit_data"),
    path('update_data/<int:dataid>/',views.update_data,name="update_data"),
    path('del_admin/<int:dataid>/',views.del_admin,name="del_admin"),
    path('add_category/',views.add_category,name="add_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('edit_category/<int:dataid>/',views.edit_category,name="edit_category"),
    path('update_category/<int:dataid>/',views.update_category,name="update_category"),
    path('del_category/<int:dataid>/',views.del_category,name="del_category"),
    path('add_pdts/',views.add_pdts,name="add_pdts"),
    path('display_pdts/',views.display_pdts,name="display_pdts"),
    path('save_pdts/',views.save_pdts,name="save_pdts"),
    path('edit_pdts/<int:dataid>/',views.edit_pdts,name="edit_pdts"),
    path('update_pdt/<int:dataid>/',views.update_pdt,name="update_pdt"),
    path('del_pdt/<int:dataid>/',views.del_pdt,name="del_pdt"),
    path('adminfn/',views.adminfn,name="adminfn"),
    path('loginfn/',views.loginfn,name="loginfn")

]