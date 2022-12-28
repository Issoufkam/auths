from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login

# Create your views here.
def home(request):
    return render(request, 'home.html')

User = get_user_model
def register(request):
   if request.method == "POST":
       username = request.POST['username']
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       phone = request.POST['phone']
       email = request.POST['email']
       password = request.POST['password']
       password1 = request.POST['password1']
       user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
       login(request, user)
       return redirect('home')
   return render(request, 'connection/register.html')
def loginF(request):
    return render(request, 'connection/login.html')

def logout(request):
     pass
