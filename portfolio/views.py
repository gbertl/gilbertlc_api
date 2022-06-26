
from django.shortcuts import get_object_or_404
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def index(request):
    queryset = Project.objects.all()
    serializer = ProjectSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
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
