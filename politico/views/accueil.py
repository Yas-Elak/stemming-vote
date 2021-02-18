from django.shortcuts import render
from ..forms import ContactForm
from ..models import ContactMessage
from django.contrib import messages

def index(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():

            contact_name = form.cleaned_data.get("contact_name")
            contact_email = form.cleaned_data.get("contact_email")
            contact_msg = form.cleaned_data.get("contact_msg")
            msg = ContactMessage(contact_email=contact_email, contact_name=contact_name,contact_msg=contact_msg)
            msg.save()
            messages.success(request, 'Form successfully submitted') # Any message you wish


    return render(request, "politico/accueil.html", {'form':form})
