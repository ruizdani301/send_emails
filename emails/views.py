from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .form import EmailForm
from emails.models import Email
from .send_email import send_email



class EmailsView(FormView):
    
    """
        The EmailsView class is a FormView that handles form submission, creates an Email object with the
        submitted data, and sends an email to the submitted email address.
    """
    template_name = "form.html"
    form_class = EmailForm
    success_url = reverse_lazy("app_emails:thank")

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        try:
            Email.objects.create(name=name, email=email)
        except Exception as e:
            print(f"Error creating email: {e}")
        send_email(name, email)
       
        return super().form_valid(form)


class ThankView(TemplateView):
    template_name = 'bye.html'
    