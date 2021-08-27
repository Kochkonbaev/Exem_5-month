from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout

from account.forms import LoginForm, RegistrationForm



class LoginView(View):

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('all_posts'))

        form = LoginForm()
        context = {'form': form}
        return render(request, 'account/dashboard.html', context)

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']            
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('all_posts'))
        context = {'form': form}
        return render('account/dashboard.html', context)



class RegisterView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('new_post'))
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'account/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = form.cleaned_data['email']
            new_user.password = form.cleaned_data['password']
            new_user.confirm_password = form.cleaned_data['confirm_password']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('new_post'))
        context = {'form': form}
        return render(request, 'account/register.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('dashboard'))