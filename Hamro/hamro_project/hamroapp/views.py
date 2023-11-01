from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a success page
        else:
            error_message = "Invalid credentials"
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})



def landing_page(request):
    return render(request, 'index.html')
