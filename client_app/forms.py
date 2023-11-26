from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}) , required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}) , required=True)






