from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def send_account_activation_email(email, email_token):
    try:
        subject = 'Activate / Verify Your Account'
        message = f'Hi,\n\nPlease click the link below to verify your email and activate your account:\n\n http://localhost:8000/accounts/activate/{email_token}\n\nThank you!'
        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, from_email, [email])
        # Get the relative URL path for activation, activate-account url ka name set h urls.py me
        # activation_path = reverse('activate-account', kwargs={'email_token': email_token})
        # # Add domain name (SITE_URL) in front of it
        # activation_link = settings.SITE_URL + activation_path
        # message = f'Hi,\n\nPlease click the link below to verify your email and activate your account:\n\n{activation_link}\n\nThank you!'

        print(f"Activation email sent to {email}")
    except Exception as e:
        print(f"Failed to send activation email: {e}")
