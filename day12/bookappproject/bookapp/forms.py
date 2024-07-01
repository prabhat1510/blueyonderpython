from django import forms

class LoginForm(forms.Form):
    username =  forms.CharField(max_length =100)
    password = forms.CharField(widget = forms.PasswordInput())


class RegisterForm(forms.Form):
    fName = forms.CharField(max_length =50)
    lName = forms.CharField(max_length =50)
    email = forms.CharField(max_length = 50)
    username =  forms.CharField(max_length =30)
    password = forms.CharField(widget = forms.PasswordInput())