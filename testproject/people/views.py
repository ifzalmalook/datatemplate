from django.shortcuts import render, redirect
from .models import Person

# Create your views here.

def index(request):
    people = Person.objects.all()
    context = {"people" : people}
    return render(request, "people/index.html", context)

def add_person(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        Person.objects.create(first_name=first_name, last_name=last_name)

        return redirect("index")