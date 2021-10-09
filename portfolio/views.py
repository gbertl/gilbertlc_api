from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from portfolio.serializers import CategorySerializer, ProjectSerializer
from .models import Project, Category


@api_view(['GET'])
def projects(request):
    projects = Project.objects.order_by('priority_order')
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def project_detail(request, pk):
    if request.method == 'PATCH':
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def categories(request):
    categories = Category.objects.order_by('id')
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)

    
