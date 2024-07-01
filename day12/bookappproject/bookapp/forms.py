from django import forms

class LoginForm(forms.Form):
    username =  forms.CharField(max_length =100)
    password = forms.CharField(widget = forms.PasswordInput())


class RegisterForm(forms.Form):
    fName = forms.CharField(max_length =100)
    lName = forms.CharField(max_length =100)
    email = forms.EmailField(max_length =100)
    username =  forms.CharField(max_length =100)
    password = forms.CharField(widget = forms.PasswordInput())