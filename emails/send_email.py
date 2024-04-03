from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(name, email) -> None:
    """
    The function `send_email` sends an email with a customized
    template to a specified recipient.
    :param name: The `name` parameter  is a string that represents
    the name of the recipient to whom the email will be sent.
    This name will be used in the email content to
    personalize the message
    :param email: The `email` parameter is a string that
    represents the email address of the recipient
    """
    # render the template that will be sent in the body
    body = render_to_string('thanks.html', {'name': name})
    subject, from_email, to = "resources", "ruizdani301@gmail.com", f'{email}'
    text_content = f"thank you {name} for requesting the resource."
    html_content = body
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file("resources/ORM.pdf")
    try:
        msg.send(fail_silently=False)
    except Exception as e:
        print(f"Error sending email: {e}")
