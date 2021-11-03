from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FormParser
from drf_nested_forms.parsers import NestedMultiPartParser

from portfolio.serializers import (
    CategorySerializer,
    ProjectReadSerializer,
    ProjectSerializer,
    RoleSerializer,
    ScreenshotSerializer,
    TechnologySerializer,
)
from .models import Project, Category, Role, Screenshot, Technology


@api_view()
def projects(request):
    projects = Project.objects.order_by('priority_order')
    serializer = ProjectReadSerializer(projects, many=True)

    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
@parser_classes([NestedMultiPartParser, FormParser])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view()
def categories(request):
    categories = Category.objects.order_by('id')
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view()
def role_list(request):
    queryset = Role.objects.all()
    serializer = RoleSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def technology_list(request):
    queryset = Technology.objects.all()
    serializer = TechnologySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def screenshot_list(request):
    queryset = Screenshot.objects.all()
    serializer = ScreenshotSerializer(queryset, many=True)
    return Response(serializer.data)
