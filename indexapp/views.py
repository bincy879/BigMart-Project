from django.shortcuts import render,redirect
from indexapp.models import Admin, Category, Products
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def index_fn(request):
    return render(request,"index.html")

def add_data(request):
    return render(request,"add_admin.html")

def save_data(request):
    if request.method=="POST":
        na=request.POST.get('pname')
        mo=request.POST.get('pmob')
        em=request.POST.get('pemail')
        im=request.FILES['pimg']
        us=request.POST.get('user')
        pwd=request.POST.get('pswd')
        cpwd=request.POST.get('cpswd')
        obj=Admin(Name=na,Mob=mo,Email_id=em,Image=im,User=us,Password=pwd,Confirm=cpwd)
        obj.save()
        return redirect(add_data)

def display_admin(request):
    data=Admin.objects.all()
    return render(request,"display_admin.html",{'data': data})

def edit_data(request,dataid):
    data=Admin.objects.get(id=dataid)
    print(data)
    return render(request,"edit_admin.html",{'data':data})

def update_data(request,dataid):
    if request.method=="POST":
        na=request.POST.get('pname')
        mo=request.POST.get('pmob')
        em=request.POST.get('pemail')
        us = request.POST.get('user')
        pwd = request.POST.get('pswd')
        cpwd = request.POST.get('cpswd')
        try:
            img=request.FILES['pimg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Admin.objects.get(id=dataid).Image
        Admin.objects.filter(id=dataid).update(Name=na,Mob=mo,Email_id=em,User=us,Password=pwd,Confirm=cpwd,Image=file)
        return redirect(display_admin)

def del_admin(request,dataid):
    data=Admin.objects.filter(id=dataid)
    data.delete()
    return redirect(display_admin)

def add_category(request):
    return render(request,"add_category.html")

def display_category(request):
    data=Category.objects.all()
    return render(request,"view_category.html",{'data':data})

def save_category(request):
    if request.method=="POST":
        na=request.POST.get('cname')
        des=request.POST.get('desc')
        im=request.FILES['cimg']
        obj=Category(C_Name=na,Description=des,C_Image=im)
        obj.save()
        return redirect(add_category)

def edit_category(request,dataid):
    data = Category.objects.get(id=dataid)
    print(data)
    return render(request, "edit_category.html", {'data': data})

def update_category(request,dataid):
    if request.method=="POST":
        na=request.POST.get('cname')
        des=request.POST.get('desc')
        try:
            im=request.FILES['cimg']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=dataid).C_Image
        Category.objects.filter(id=dataid).update(C_Name=na,Description=des,C_Image=file)
        return redirect(display_category)

def del_category(request,dataid):
    data=Category.objects.filter(id=dataid)
    data.delete()
    return redirect(display_category)

def add_pdts(request):
    data=Category.objects.all()
    return render(request,"add_pdts.html",{'data':data})

def display_pdts(request):
    data=Products.objects.all()
    return render(request,"display_pdts.html",{'data':data})

def save_pdts(request):
    if request.method=="POST":
        na=request.POST.get('pname')
        pr=request.POST.get('price')
        qy=request.POST.get('qnty')
        de=request.POST.get('desc')
        im=request.FILES['imge']
        ca=request.POST.get('categry')
        obj=Products(P_Name=na,Price=pr,Qty=qy,Descr=de,P_Image=im,Category=ca)
        obj.save()
        return redirect(add_pdts)

def edit_pdts(request,dataid):
    data=Products.objects.get(id=dataid)
    data1=Category.objects.all()
    print(data)
    return render(request,"edit_pdts.html",{'data':data,'data1':data1})

def update_pdt(request,dataid):
    if request.method=="POST":
        na=request.POST.get('pname')
        pr=request.POST.get('price')
        qy=request.POST.get('qnty')
        de=request.POST.get('desc')
        try:
            im = request.FILES['imge']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = Products.objects.get(id=dataid).P_Image
        ca = request.POST.get('categry')
        Products.objects.filter(id=dataid).update(P_Name=na, Price=pr, Qty=qy, Descr=de, P_Image=file,Category=ca)
        return redirect(display_pdts)

def del_pdt(request,dataid):
    data=Products.objects.filter(id=dataid)
    data.delete()
    return redirect(display_pdts)

def adminfn(request):
    return render(request,"loginpage.html")

def loginfn(request):
    if request.method=="POST":
        username_r=request.POST.get('user')
        password_r=request.POST.get('pwd')

        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['user']=username_r
                request.session['pwd']=password_r
                return redirect(index_fn)
            else:
                return redirect(adminfn)
        else:
            return redirect(adminfn)






