from rest_framework import serializers
from .models import Category, Project, Screenshot, Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    screenshots = serializers.PrimaryKeyRelatedField(queryset=Screenshot.objects.all(), many=True)

    class Meta:
        model = Project
        fields = '__all__'
