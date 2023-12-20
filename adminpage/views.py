from django.shortcuts import render
from userpage.models import *
from django.contrib.auth.decorators import login_required
from userpage.auth import admin_only

# Create your views here.

def admin_dashboard(request):
    return render(request,'admin/dashboard.html')



def user_order(request):
    user=request.user
    order=Order.objects.all()
    context={
        'items':order 
    }
    return render(request,'admin/order.html',context)