

def send_registration_email(user):
    subject = "SignUp Success"
    message = f"Congratulations {user.first_name}. You have successfully created your account"
    user.email_user(subject=subject, message=message, from_email="noreply@gmail.com")
