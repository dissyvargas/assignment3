
from django.shortcuts import render, get_object_or_404
from .models import Degree, requiredCourses, degreeSpecific

def index(request):
    return render(request, "course_list.html")

def class_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})

def course_list(request):
    courses = requiredCourses.objects.all()
    course_list = []
    for course in courses:
        course_list.append({'course': course})

    context = {
        'course_list': course_list
    }
    return render(request, 'degree_checklist/course_list.html', context)