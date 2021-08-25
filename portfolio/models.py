from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)

class Technology(models.Model):
    name = models.CharField(max_length=50)

class Screenshot(models.Model):
    image = models.ImageField()

class Category(models.Model):
    name = models.CharField(max_length=50)

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.IntegerField()
    roles = models.ManyToManyField(Role)

    technologies = models.ManyToManyField(Technology)

    live_preview = models.URLField(blank=True)
    source_code = models.URLField()

    thumbnail = models.ImageField()
    screenshots = models.ManyToManyField(Screenshot)

    categories = models.ManyToManyField(Category)
