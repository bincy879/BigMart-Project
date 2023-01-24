from django.shortcuts import render,redirect
from indexapp.models import Category,Products,Contact
from front_end.models import registration_db
# Create your views here.
def home(request):
    da=Category.objects.all()
    return render(request,"home.html",{'da':da})

def aboutfn(request):
    da = Category.objects.all()
    return render(request, "about.html", {'da': da})

def productsfn(request):
    data = Products.objects.all()
    da=Category.objects.all()
    return render(request, "products.html", {'data': data , 'da':da})

def disCat(request,itemCatg):
    print("===itemCatg===",itemCatg)
    catg=itemCatg.upper()
    da=Category.objects.all()
    products=Products.objects.filter(Category=itemCatg)
    context={
        'products':products,
        'catg':catg,
        'da':da
    }
    return render(request,"display_cat.html",context)

def show_pdt_detls(request,dataid):
    dat=Products.objects.get(id=dataid)
    return render(request,"show_pdt_details.html",{'dat':dat})

def registr(request):
    return render(request,"registr_page.html")

def registr_save(request):
    if request.method=="POST":
        us=request.POST.get('user')
        em=request.POST.get('email')
        pd=request.POST.get('pwd')
        cpd=request.POST.get('cpwd')
        if pd==cpd:
            obj=registration_db(Username=us,Email=em,Password=pd,C_password=cpd)
            obj.save()
            return redirect(registr)
        else:
            return render(request,"registr_page.html",{'msg':"Sorry..password doesn't match!!"})

def login(request):
    return render(request,"login_page.html")

def login_save(request):
    if request.method=="POST":
        us=request.POST.get('usr')
        pwd=request.POST.get('pswd')
        if registration_db.objects.filter(Username=us,Password=pwd).exists():
            request.session['usr']=us
            request.session['pwd']=pwd

            return redirect(home)
        else:
            return render(request,"login_page.html",{'msg':"Invalid username or password!!"})

def logout(request):
    del request.session['usr']
    del request.session['pwd']
    return redirect(home)

def contact(request):
    return render(request,"contact.html")

def msgSave(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        su=request.POST.get('subj')
        ms=request.POST.get('mesg')
        obj=Contact(Name=na,Email=em,Sub=su,Msg=ms)
        obj.save()
        return redirect(contact)


