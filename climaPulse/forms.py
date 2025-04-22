from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import BlogPost
from ckeditor.widgets import CKEditorWidget

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BlogPostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    content = forms.CharField(
        label="Content",
        widget=CKEditorWidget(attrs={'class': 'form-control'}),  # CKEditor comes with its own styles
    )
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
