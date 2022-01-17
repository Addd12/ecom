from django.shortcuts import render
from index.forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New message from {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            send_mail(email_subject, email_message, from_email, settings.ADMIN_EMAIL)
            messages.success(request, f'Your message is sent!')
    form = ContactForm()
    context = {'form': form}
    return render(request, "index/about.html", context)
