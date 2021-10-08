from django.shortcuts import render
from . models import *

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")       
        email = request.POST.get("email", "")
        phone_no = request.POST.get("phone_no", "")
        message = request.POST.get("message", "")

        email_context = {
            "name":name,
            "email":email,
            "phone_no":phone_no,
            "message":message
            
        }
        template_email = render_to_string('email_template.html', email_context)

        email_obj = EmailMessage(

            name + "has sent an email",
            template_email,
            settings.EMAIL_HOST_USER,
            ['aparabiswas28@gmail.com', 'kalitaluna28@gmail.com']

        )
        email_obj.fail_silently = False
        email_obj.send()
        # print(email_obj)

    return render(request, 'contact.html')