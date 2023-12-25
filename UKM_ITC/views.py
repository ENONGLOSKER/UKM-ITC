from django.shortcuts import render,redirect, get_object_or_404
from ITC_APP . models import Anggota,Notification,Bidang,Event,Pengurus
from ITC_APP. forms import AnggotaForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login,logout
from datetime import date
from django.core.paginator import Paginator


@csrf_exempt
def index(request):
    data = Anggota.objects.filter(diverifikasi=True).order_by('-id')
    # Implementasi pagination
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'data':data,
        'datas': page_obj,
    }
    return render(request,'index.html',context)

@csrf_exempt
def dash(request):
    anggota = Anggota.objects.all().order_by('-diverifikasi')
    context={
        'anggota':anggota
    }
    return render(request,'dash.html',context)

@csrf_exempt
def form_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            messages.success(request,"Selamat, Login Berhasil!")
            return redirect('dashboard:dashboard')
        elif user is not None and user.is_staff:
            login(request, user)
            messages.success(request,"Selamat, Login Berhasil!")
            return redirect('dash')
        else:
            return redirect('form_login')

    return render(request, 'form_login.html')
    
@csrf_exempt
def form_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('form_login')

@csrf_exempt
def sukses_home(request):
    return render(request, 'sukses_home.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = AnggotaForm(request.POST)
        if form.is_valid():
            anggota = form.save()
            
            Notification.objects.create(
                message=f'Anggota baru "{form.instance.nama}" ditambahkan!',
                notification_type='new_member'
            )
            return redirect('sukses')
    else:
        form = AnggotaForm()
    return render(request, 'form_anggota.html', {'form': form})