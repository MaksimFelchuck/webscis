from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=40)


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    user_last_name = forms.CharField(label='user_last_name', max_length=100)
    email = forms.EmailField(label='email', max_length=40)
    password = forms.CharField(label='Password', max_length=40)
