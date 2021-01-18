from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'username':
                field.widget.attrs['minlength'] = 5
            field.widget.attrs['class'] = 'form-control'

            if field_name == 'password':
                field.widget.attrs['minlength'] = 8


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget.attrs['minlength'] = 8
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self, **kwargs):
        user = super(UserRegisterForm, self).save()
        user.save()
        return user


class UserEditFrom(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def __init__(self, *args, **kwargs):
        super(UserEditFrom, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def save(self, **kwargs):
        user = super(UserChangeForm, self).save()
        user.save()
        return user
