from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages

# Create your views here.
def about_me(request):

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            collaborate_form = CollaborateForm()
            messages.add_message(request, messages.SUCCESS, 'Collaboration request received! I endeavour to respond within 2 working days.')

    return render(
        request,
        "about/about.html",
        {"about": about,
        "collaborate_form": collaborate_form},
    )

