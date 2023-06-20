from django.shortcuts import render

import product.models
from .forms import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        return super().form_valid(form)


# class LoginView(FormView):
#     template_name = 'login.html'  # template_name이라고 하면 html파일이조? 이게 부모인 FormView에서 가져온거에요.
#     form_class = LoginForm
#     success_url = '/'


def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 로그인 후 리다이렉트할 URL 설정
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

