from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        avatar = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'avatar')

class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = 'Неверный логин или пароль'
    
    password = forms.CharField(
        label='Пароль',
        max_length=100,
        widget=forms.PasswordInput()
    )
    
    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'avatar'
        )