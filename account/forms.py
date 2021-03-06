from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label= 'Почта', widget=forms.EmailInput())
    password = forms.CharField(label= 'Пароль',widget=forms.PasswordInput())
        
    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Почта'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтверждения пароля'

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['ru', 'net']:
            raise forms.ValidationError(f'Домен {domain} не доступен для регистрации')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный адрес уже зарегестрирован в системе')
        return email

    def clean(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data['password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'confirm_password',)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
