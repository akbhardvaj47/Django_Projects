from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    # Password ke liye input field, jisme typing hidden hoti hai
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User  # Ye form User model se linked hai
        # Ye fields form me dikhengi
        fields = ['username', 'email', 'password']

    # Password aur Confirm password ko match karne ke liye
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
