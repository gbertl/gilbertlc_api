from graphene_django import DjangoObjectType
import graphene
from portfolio.models import Category, Project, Screenshot, Technology

class TechnologyNode(DjangoObjectType):
    class Meta:
        model = Technology

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category

class ScreenshotNode(DjangoObjectType):
    class Meta:
        model = Screenshot

class ProjectNode(DjangoObjectType):
    technology_list = graphene.List(graphene.String)
    category_list = graphene.List(graphene.String)
    screenshot_list = graphene.List(graphene.String)

    class Meta:
        model = Project

    def resolve_technology_list(self, _):
        return [tech.name for tech in self.technologies.all()]

    def resolve_category_list(self, _):
        return [category.name for category in self.categories.all()]

    def resolve_screenshot_list(self, _):
        return [sc.image.url for sc in Screenshot.objects.filter(project_id=self.id)]


class Query(graphene.ObjectType):
    projects = graphene.List(ProjectNode)
    categories = graphene.List(CategoryNode)


    def resolve_projects(self, _):
        return Project.objects.all()

    def resolve_categories(self, _):
        return Category.objects.all()

schema = graphene.Schema(query=Query)
