from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def projects(request):
    return render(request, 'main/projects.html')

def achievements(request):
    return render(request, 'main/achievements.html')

def education(request):
    return render(request, 'main/education.html')

def skills(request):
    return render(request,'main/skills.html')