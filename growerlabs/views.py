from django.shortcuts import render, HttpResponse
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

def about(request):
    profile = Profile.objects.all()
    context = {
        "profile":profile,
    }
    return render(request, 'about.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        "projects":projects,
    }
    return render(request, 'projects.html', context)    

def profile(request, pk):
    prof = Profile.objects.filter(pk=pk)[0]

    if prof.github_link is not None:
        user_name = prof.github_link.split('/')[3]
        return render(request,"profile.html", { "prof":prof, "user_name":user_name })
    
    else:
        return render(request,"profile.html", { "prof":prof })

  