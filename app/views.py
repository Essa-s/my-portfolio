from django.shortcuts import render

# Create your views here.
from .models import BasicInfo, Skill, Course, Education, Experience, Fact, Service, Project

def home(request):
    basic_info = BasicInfo.objects.first()  # Assuming you have retrieved the BasicInfo object
    skills = Skill.objects.all()
    facts = Fact.objects.all()
    courses = Course.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()

    context = {
        'basic_info': basic_info,
        'skills': skills,
        'facts': facts,
        'courses': courses,
        'educations': educations,
        'experiences': experiences,
        'services': services,
        'projects': projects,

    }
    return render(request, 'index.html', context)

