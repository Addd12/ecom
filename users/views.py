from django.shortcuts import redirect, render
#from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login') # it was render instead of redirect and it gave error: TemplateDoesNotExist at /register/
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {'form': form})

# def login(request):
#     return render(request, 'users/login.html')
