from django import forms
from .models import Book,Reg

#library
class BookCreate(forms.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'

class RegForm(forms.ModelForm):
    class Meta:
        password=forms.CharField(widget=forms.PasswordInput)
        model=Reg
        widgets={'pwd':forms.PasswordInput()}
        fields=['user','pwd']
        labels={'user':'USERNAME','pwd':'PASSWORD'}
class LoginForm(forms.Form):
    user=forms.CharField(max_length=20)
    pwd=forms.CharField(widget=forms.PasswordInput())
    labels={'user':'USERNAME','pwd':'PASSWORD'}
