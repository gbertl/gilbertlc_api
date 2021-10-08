from rest_framework.decorators import api_view
from rest_framework.response import Response

from portfolio.serializers import CategorySerializer, ProjectSerializer
from .models import Project, Category


@api_view(['GET'])
def index(request):
    projects = Project.objects.order_by('priority_order')
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def categories(request):
    categories = Category.objects.order_by('id')
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)
