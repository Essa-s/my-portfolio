from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BasicInfo, Skill, Course, Education, Experience, Fact, Service, Project

def home(request):
    basic_info = BasicInfo.objects.first()  # Assuming you have retrieved the BasicInfo object
    skills_1 = Skill.objects.all().order_by('id')[:3]   #here to sort it in html for each 3
    skills_2 = Skill.objects.all().order_by('id')[3:]   # last 3
    facts = Fact.objects.all()
    courses = Course.objects.all()
    education = Education.objects.all()
    last_education_degree = Education.objects.last().degree #get last degree from education
    experiences = Experience.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()

    context = {
        'basic_info': basic_info,
        'skills_1': skills_1,
        'skills_2': skills_2,
        'facts': facts,
        'courses': courses,
        'education': education,
        'experiences': experiences,
        'services': services,
        'projects': projects,
        'last_education_degree': last_education_degree

    }
    return render(request, 'index.html', context)

