from rest_framework import serializers
from .models import Project, Category, Role, Screenshot, Technology


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Role
        fields = '__all__'


class TechnologySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Technology
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'name': {'validators': []}}

    def validate(self, data):
        query = Category.objects.filter(name=data.get('name'))
        if 'id' in data:
            query = query.exclude(id=data.get('id'))
        if query.exists():
            raise serializers.ValidationError(
                {'name': 'A category with this name already exists'}
            )

        return super().validate(data)


class ScreenshotSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Screenshot
        fields = '__all__'
        extra_kwargs = {'image': {'required': False}, 'project': {'read_only': True}}

    def to_internal_value(self, data):
        if 'id' in data:
            if not hasattr(data.get('image'), 'read'):
                data.pop('image')
        else:
            if not data.get('image'):
                raise serializers.ValidationError({'image': 'No file was submitted.'})

        return super().to_internal_value(data)


class ProjectSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    technologies = TechnologySerializer(many=True)
    categories = CategorySerializer(many=True)
    screenshots = ScreenshotSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'

    def to_internal_value(self, data):
        if self.instance:
            # convert {'[]': ''} (which means empty array) to []
            # supports 1 depth
            for k in data.keys():
                try:
                    if data[k]['[]'] == '':
                        data[k] = []
                except (KeyError, TypeError):
                    pass

        return super().to_internal_value(data)

    def update_or_create_m2m(self, model, m2m, data):
        if self.partial and data is None:
            return

        objs = []

        for d in data:
            obj, _ = model.objects.update_or_create(id=d.get('id'), defaults=d)
            objs.append(obj)

        m2m.set(objs)

    def update(self, instance, validated_data):
        roles_data = validated_data.pop('roles', None)
        technologies_data = validated_data.pop('technologies', None)
        categories_data = validated_data.pop('categories', None)
        screenshots_data = validated_data.pop('screenshots', None)

        instance = super().update(instance, validated_data)

        self.update_or_create_m2m(Role, instance.roles, roles_data)
        self.update_or_create_m2m(Technology, instance.technologies, technologies_data)
        self.update_or_create_m2m(Category, instance.categories, categories_data)

        for i, sd in enumerate(screenshots_data):
            if not sd['priority_order']:
               sd['priority_order'] = screenshots_data[i if i == 0 else i - 1]['priority_order'] + 1
        self.update_or_create_m2m(Screenshot, instance.screenshots, screenshots_data)

        return instance


class ProjectReadSerializer(ProjectSerializer):
    roles = serializers.StringRelatedField(many=True)
    technologies = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)
    screenshots = serializers.StringRelatedField(many=True)
