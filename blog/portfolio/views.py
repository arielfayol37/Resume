from django.shortcuts import render
from .models import Project, Experience, Skill, Award

# Create your views here.

def home(request):
    about_me = (
        "Hi, I'm Ariel Fayol Ateufack, a researcher and developer passionate about technology, "
        "problem-solving, and sharing knowledge. Welcome to my portfolio!"
    )
    projects = Project.objects.all()[:3]  # Show top 3 projects
    experiences = Experience.objects.all().order_by('-start_date')
    skills = Skill.objects.all()
    awards = Award.objects.all().order_by('-date')

    context = {
        'about_me': about_me,
        'projects': projects,
        'experiences': experiences,
        'skills': skills,
        'awards': awards,
    }
    return render(request, 'portfolio/index.html', context)
