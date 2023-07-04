from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .mixins import LoginMixin
from .models import User

from .forms import (
    MyUserCreationForm, 
    MyAuthenticationForm,
    UserUpdateForm
)


class RegisterView(View):
    def get(self, request):
        form = MyUserCreationForm()
        return render(request, 'auths/register.html', {'form': form})

    def post(self, request):
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if 'avatar' in request.FILES:
                user.avatar = request.FILES['avatar']
            user.save()
            return redirect('login')
        return render(request, 'auths/register.html', {'form': form})
    


class LoginView(View):
    def get(self, request):
        form = MyAuthenticationForm()
        return render(request, 'auths/login.html', {'form': form})

    def post(self, request):
        form = MyAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('protected')
        return render(request, 'auths/login.html', {'form': form})

class ProtectedView(LoginMixin, View):
    def get(self, request):
        return render(request, 'main/protected.html')


class UpdateUserView(LoginMixin, View):
    def get(self, request):
        form = UserUpdateForm()
        return render(request, 'auths/edit.html', context={'form': form})

    def post(self, request, username):
        if request.method == 'POST':
            user = request.user
            form = UserUpdateForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                user_form = form.save()
                return redirect('protected', user_form.username)
            
        user = User.objects.filter(username=username).first()
        if user:
            form = UserUpdateForm(instance=user)
            form.fields['username']
            return render(
                request=request,
                template_name='auths/edit.html',
                context={'form': form}
            )
        return redirect('protected')

class LogoutView(LoginMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
