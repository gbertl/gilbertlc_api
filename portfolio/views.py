from django.http import JsonResponse

from portfolio.serializers import CategorySerializer, ProjectSerializer
from .models import Project, Category


def index(request):
    projects = Project.objects.order_by('priority_order')
    serializer = ProjectSerializer(projects, many=True)

    return JsonResponse(serializer.data, safe=False)


def categories(request):
    categories = Category.objects.order_by('id')
    serializer = CategorySerializer(categories, many=True)

    return JsonResponse(serializer.data, safe=False)
