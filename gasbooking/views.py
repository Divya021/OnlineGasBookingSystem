from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
import datetime
from datetime import date


def home(request):
    return render(request,'carousel.html')

def Admin_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "yes"
                return redirect('admin_home')
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'login.html',d)
def Admin_Home(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    return render(request, 'admin_home.html')
def User_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if not user.is_staff:
                login(request, user)
                return redirect('user_home')
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'user_login.html',d)
def Signup(request):
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        m=request.POST['mobile']
        e=request.POST['email']
        user=User.objects.create_user(username=u,password=p,email=e)
        sign=Registration.objects.create(mobile=m,user=user)
        return redirect('login')
    return render(request,'signup.html')
def New_connection(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    br=""
    rt = datetime.datetime.now()
    rd = datetime.date.today()
    rt1 = str(rt).split(":")
    rt2 = "".join(rt1)
    order_id1 = rt2.split("-")
    order_id2 = "".join(order_id1)
    order_id3 = order_id2.split(" ")
    order_id4 = "".join(order_id3)
    order_id = order_id4.replace("2020","")
    data=Registration.objects.get(user=request.user.id)
    if request.method == "POST":
        u = request.POST['uname']
        e= request.POST['email']
        mo = request.POST['mobile']
        g = request.POST['gender']
        n = request.POST['nationality']
        m= request.POST['married']
        a = request.POST['add']
        r = request.POST['ralated']
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['city']
        z = request.POST['zipcode']
        i= request.FILES['img']
        b=User.objects.get(username=u,email=e)
        br=Registration.objects.get(user=b,mobile=mo)
        Newconnection.objects.create(user=br,gen=g,connection='null',date=date.today(),cost='null',registration=order_id,nationality=n,merriedstatus=m,address=a,related=r,fname=f,lname=l,city=c,zipcode=z,img=i)
        error = True
        return redirect('view_connection')
    d={'data':data,'error':error}
    return render(request,'new_connection.html',d)
def user_Home(request):
    return render(request, 'user_home.html')
def View_connection(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.filter(user=data)
    d={'data1':data1}
    return render(request,'view_connection.html',d)
def admin_viewbooking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data1=Bookcylinder.objects.all()
    d={'data1':data1}
    return render(request,'admin_viewbooking.html',d)

def edit_connection(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.get(user=data)
    error=False
    if request.method=="POST":
        u = request.POST['uname']
        e= request.POST['email']
        mo = request.POST['mobile']
        g = request.POST['gender']
        n = request.POST['nationality']
        m= request.POST['married']
        a = request.POST['add']
        r = request.POST['ralated']
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['city']
        z = request.POST['zipcode']
        i= request.FILES['img']

        try:
            i= request.FILES['image']
            data1.img=i
            data1.save()
        except:
            pass
        user.username=u
        user.email=e
        data.mobile=mo
        data1.gen=g
        data1.nationality=n
        data1.merriedstatus=m
        data1.related=r
        data1.fname=f
        data1.rname=l
        data1.city=c
        data1.zipcode=z
        data1.save()
        data.save()
        user.save()
        error=True
        return redirect('view_connection')
    d={'data1':data1,'error':error,'data':data,}
    return render(request,'edit_connection.html',d)

def Logout(request):
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)

def admin_viewconnection(request):
    data=Newconnection.objects.all()
    d={'data':data}
    return render(request,'admin_viewconnection.html',d)
def Admin_connection(request,pid):
    data=Newconnection.objects.get(id=pid)
    d={'data':data}
    return render(request,'admin_connectiondetail.html',d)
def Edit_status(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    book =Newconnection.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST['status']
        c = request.POST['cost']
        book.connection = s
        book.cost= c
        book.save()
        return redirect('admin_viewconnection')
    d = {'book': book,}
    return render(request,'edit_status.html', d)
def bookcylinder(request):
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.filter(user=data)
    d={'data1':data1}
    return render(request,'bookingcylinder.html',d)
def bookdetail(request):
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.filter(user=data)
    d={'data1':data1}
    return render(request,'bookdetail.html',d)
def book(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.get(user=data)
    rt = datetime.datetime.now()
    rd = datetime.date.today()
    rt1 = str(rt).split(":")
    rt2 = "".join(rt1)
    order_id1 = rt2.split("-")
    order_id2 = "".join(order_id1)
    order_id3 = order_id2.split(" ")
    order_id4 = "".join(order_id3)
    order_id = order_id4.replace("2020","")
    if request.method == "POST":
        g = request.POST['gassize']
        Bookcylinder.objects.create(user=data1,gassize=g,booknumber=order_id,bookdate=date.today(),bookstatus='null',reffercost='null',assignto='null',responsetime='null')
    d={'data1':data1}
    return render(request,'book.html',d)
def View_booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data2=Newconnection.objects.get(user=data)
    data1=Bookcylinder.objects.filter(user=data2)
    d={'data1':data1}
    return render(request,'view_booking.html',d)
def bookhistory(request):
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data2=Newconnection.objects.get(user=data)
    data1=Bookcylinder.objects.filter(user=data2)
    d={'data1':data1}
    return render(request,'bookhistory.html',d)
def Admin_booking(request,pid):
    data=Bookcylinder.objects.get(id=pid)
    d={'data':data}
    return render(request,'admin_bookingdetail.html',d)
def Edit_booking(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    book =Bookcylinder.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST['bookstatus']
        a = request.POST['assignto']
        r= request.POST['reffercost']
        book.bookstatus = s
        book.assignto= a
        book.reffercost= r
        book.responsetime= date.today()
        book.save()
        return redirect('admin_viewbooking')
    d = {'book': book,}
    return render(request,'edit_booking.html', d)
def addstaff(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    if request.method == "POST":
        i = request.POST['staffid']
        n = request.POST['name']
        e= request.POST['email']
        m= request.POST['mobile']
        a= request.POST['address']
        Addstaff.objects.create(staffid=i,email=e,mobile=m,name=n,address=a)
        return redirect('admin_home')
    return render(request,'addstaff.html')
def view_staff(request):
     if not request.user.is_staff:
        return redirect('admin_login')
     data=Addstaff.objects.all()
     d={'data':data}
     return render(request,'view_staff.html',d)

def edit_staff(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    data=Addstaff.objects.get(id=pid)
    if request.method == "POST":
        i = request.POST['staffid']
        n = request.POST['name']
        e= request.POST['email']
        m= request.POST['mobile']
        a= request.POST['address']
        data.staffid=i
        data.name=n
        data.email=e
        data.mobile=m
        data.address=a
        data.save()
        return redirect('view_staff')
    d={'data':data}
    return render(request,'edit_staff.html',d)
def delete_staff(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    data=Addstaff.objects.get(id=pid)
    data.delete()
    return redirect('view_staf')


