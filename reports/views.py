from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Report
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def home(request):
    return render(request,"home.html")
def addnew(request):
    if request.method == "POST":
        custom_id = request.POST.get('id')
        house_no = request.POST.get('house_no')
        address = request.POST.get('address')
        village = request.POST.get('village')
        client_name = request.POST.get('client_name')
        type = request.POST.get('type')
        sub_type = request.POST.get('property_type')  # ✅ correct name
        lic_agent_name = request.POST.get('agent_name')
        estimate_status = request.POST.get('estimate_status')
        client_mobile = request.POST.get('mobile')  # ✅ correct name
        file_status = request.POST.get('file_status')
        date = request.POST.get('date')

        Report.objects.create(
            user=request.user,
            custom_id=custom_id,
            house_no=house_no,
            address=address,
            village=village,
            client_name=client_name,
            type=type,
            sub_type=sub_type,
            lic_agent_name=lic_agent_name,
            estimate_status=estimate_status,
            client_mobile=client_mobile,
            file_status=file_status,
            date=date
        )
        messages.success(request, "✅ Data Saved Successfully!")
        return redirect('home')  # save ke baad home pe bhej dega
    return render(request,'add.html')
def search(request):
    reports = Report.objects.filter(user=request.user)
    if request.method == "POST":
        custom_id = request.POST.get('custom_id')
        client_name = request.POST.get('client_name')
        lic_agent_name = request.POST.get('lic_agent_name')
        type = request.POST.get('type')
        estimate_status = request.POST.get('estimate_status')
        file_status = request.POST.get('file_status')

        if custom_id:
            reports = reports.filter(custom_id__icontains=custom_id)

        if client_name:
            reports = reports.filter(client_name__icontains=client_name)

        if lic_agent_name:
            reports = reports.filter(lic_agent_name__icontains=lic_agent_name)

        if type:
            reports = reports.filter(type=type)

        if estimate_status:
            reports = reports.filter(estimate_status=estimate_status)

        if file_status:
            reports = reports.filter(file_status=file_status)

    return render(request, 'search.html', {'reports': reports})
def edit_record(request, id):
    
    # 🔹 record fetch
    record = get_object_or_404(Report, id=id, user=request.user)
    if request.method == "POST":

        record.custom_id = request.POST.get('custom_id')
        record.house_no = request.POST.get('house_no')
        record.address = request.POST.get('address')
        record.village = request.POST.get('village')
        record.client_name = request.POST.get('client_name')
        record.type = request.POST.get('type')
        record.sub_type = request.POST.get('sub_type')
        record.lic_agent_name = request.POST.get('lic_agent_name')
        record.estimate_status = request.POST.get('estimate_status')
        record.client_mobile = request.POST.get('client_mobile')
        record.file_status = request.POST.get('file_status')
        record.date = request.POST.get('date')

        record.save()

        return redirect('search')  # save ke baad search page pe

    return render(request, 'edit.html', {'record': record})
def delete(request,id):
    r = get_object_or_404(Report, id=id, user=request.user)
    r.delete()
    return redirect('search')
from django.contrib.auth.forms import UserCreationForm #for creating new user

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 🔴 validations
        if password1 != password2:
            messages.error(request, "Passwords do not match ❌")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists ❌")
            return redirect("register")

        # ✅ create user (IMPORTANT)
        user = User.objects.create_user(
            username=username,
            password=password1
        )
        user.save()

        messages.success(request, "Account Created Successfully ✅")
        return redirect("login")

    return render(request, "register.html")
    
def rlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print("USER:", user)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful ✅")

            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password ❌")
            return redirect("login")
    

    return render(request, "login.html")   # 🔥 same page reload

    
# Create your views here.
