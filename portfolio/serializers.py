from rest_framework import serializers

from .models import Project, Category


class ProjectSerializer(serializers.ModelSerializer):
    roles = serializers.StringRelatedField(many=True)
    technologies = serializers.StringRelatedField(many=True)
    screenshots = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
