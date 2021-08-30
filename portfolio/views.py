from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Project, Category

def index(request):
    projects = Project.objects.order_by('priority_order')
    data = list(projects.values())


    for index, project in enumerate(projects):
        thumbnail = request.build_absolute_uri(project.thumbnail.url) 
        roles = [r.name for r in project.roles.all()]
        technologies = [t.name for t in project.technologies.all()]
        screenshots = [
            request.build_absolute_uri(ps.screenshot.image.url) 
            for ps in project.projectscreenshot_set.order_by('priority_order')
        ]
        categories = [c.name for c in project.categories.all()]

        data[index]['thumbnail'] = thumbnail
        data[index]['roles'] = roles
        data[index]['technologies'] = technologies
        data[index]['screenshots'] = screenshots
        data[index]['categories'] = categories

    return JsonResponse(data, safe=False)

def categories(request):
    categories = Category.objects.order_by('id')
    data = list(categories.values())

    return JsonResponse(data, safe=False)
