from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'technologies'

class Screenshot(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f'{self.image}'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'categories'

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.IntegerField()
    roles = models.ManyToManyField(Role)

    technologies = models.ManyToManyField(Technology)

    live_preview = models.URLField(blank=True)
    source_code = models.URLField()

    thumbnail = models.ImageField()
    screenshots = models.ManyToManyField(Screenshot, through='ProjectScreenshot')

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title}'

class ProjectScreenshot(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    screenshot = models.ForeignKey(Screenshot, on_delete=models.CASCADE)
    priority_order = models.IntegerField()

    def __str__(self):
        return f'{self.project.title} - {self.screenshot.image} ({self.priority_order})'
