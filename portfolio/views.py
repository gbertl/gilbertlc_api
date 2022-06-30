from django.shortcuts import get_object_or_404
from .models import Category, Project, Screenshot, Technology
from .serializers import (
    CategorySerializer,
    ProjectSerializer,
    ScreenshotSerializer,
    TechnologySerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .permissions import IsSuperUserOrReadOnly


@api_view()
def project_list(request):
    ordering = request.query_params.getlist('ordering[]')
    queryset = Project.objects.all()

    if len(ordering):
        queryset = Project.objects.order_by(*ordering)

    serializer = ProjectSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsSuperUserOrReadOnly])
def project_detail(request, id):
    obj = get_object_or_404(Project, id=id)

    if request.method == 'GET':
        serializer = ProjectSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(obj, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def technology_list(request):
    ids = request.query_params.getlist('ids[]')
    queryset = Technology.objects.all()

    if len(ids):
        queryset = Technology.objects.filter(id__in=ids)

    serializer = TechnologySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def category_list(request):
    ids = request.query_params.getlist('ids[]')
    queryset = Category.objects.all()

    if len(ids):
        queryset = Category.objects.filter(id__in=ids)

    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def screenshot_list(request):
    ids = request.query_params.getlist('ids[]')
    queryset = Screenshot.objects.all()

    if len(ids):
        queryset = Screenshot.objects.filter(id__in=ids)

    serializer = ScreenshotSerializer(queryset, many=True)
    return Response(serializer.data)
