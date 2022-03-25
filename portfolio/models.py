from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'technologies'


class Screenshot(models.Model):
    class Meta:
        ordering = ['priority_order']

    image = models.ImageField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.SET_NULL,
        null=True,
        related_name='screenshots',
        default='',
    )
    priority_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.image.url

class Category(models.Model):
    title = models.CharField(max_length=50)
    name = models.SlugField(unique=True)
    priority_order = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Project(models.Model):
    class Meta:
        ordering = ['priority_order']

    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.IntegerField()
    roles = models.ManyToManyField(Role)

    technologies = models.ManyToManyField(Technology)

    live_preview = models.URLField(blank=True)
    source_code = models.URLField(blank=True)

    categories = models.ManyToManyField(Category)

    priority_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.priority_order:
            self.priority_order = Project.objects.count() + 1

        super().save(*args, **kwargs)
