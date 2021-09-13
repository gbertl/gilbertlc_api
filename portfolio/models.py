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
    title = models.CharField(max_length=50)
    name = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'categories'

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.IntegerField()
    roles = models.ManyToManyField(Role)

    technologies = models.ManyToManyField(Technology)

    live_preview = models.URLField(blank=True)
    source_code = models.URLField(blank=True)

    thumbnail = models.ImageField()
    screenshots = models.ManyToManyField(Screenshot, through='ProjectScreenshot')

    categories = models.ManyToManyField(Category)

    priority_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.priority_order:
            self.priority_order = Project.objects.count() + 1

        super().save(*args, **kwargs)

class ProjectScreenshot(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    screenshot = models.ForeignKey(Screenshot, on_delete=models.CASCADE)
    priority_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.project.title} - {self.screenshot.image} ({self.priority_order})'

    def save(self, *args, **kwargs):
        if not self.priority_order:
            p = Project.objects.get(pk=self.project_id)
            self.priority_order = p.screenshots.count() + 1

        super().save(*args, **kwargs)
