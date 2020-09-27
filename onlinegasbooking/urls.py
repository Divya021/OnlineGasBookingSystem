"""onlinegasbooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gasbooking.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login',Admin_Login,name='admin_login'),
    path('admin_home',Admin_Home,name='admin_home'),
    path('user_login',User_Login,name='login'),
    path('user_home',user_Home,name='user_home'),
    path('signup',Signup,name='signup'),
    path('logout',Logout,name='logout'),
    path('adminviewconnection',admin_viewconnection,name='admin_viewconnection'),
    path('adminviewbooking',admin_viewbooking,name='admin_viewbooking'),
    path('admin_connection(?P<pid>[0-9]+)',Admin_connection,name='admin_connection'),
    path('adminbookingdetail(?P<pid>[0-9]+)',Admin_booking,name='admin_bookingdetail'),
    path('edit_status(?P<pid>[0-9]+)',Edit_status,name='edit_status'),
    path('edit_booking(?P<pid>[0-9]+)',Edit_booking,name='edit_booking'),
    path('view_connection',View_connection,name='view_connection'),
    path('bookcylinder',bookcylinder,name='bookcylinder'),
    path('newconnection',New_connection,name='newconnection'),
    path('editconnection',edit_connection,name='edit_connection'),
    path('book',book,name='book'),
    path('view_booking',View_booking,name='view_booking'),
    path('bookdetail',bookdetail,name='bookdetail'),
    path('bookhistory',bookhistory,name='bookhistory'),
    path('add_staff',addstaff,name='add_staff'),
    path('view_staff',view_staff,name='view_staff'),
    path('editstaff(?P<pid>[0-9]+)',edit_staff,name='edit_staff'),
    path('deletestaff(?P<pid>[0-9]+)',delete_staff,name='delete_staff'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
