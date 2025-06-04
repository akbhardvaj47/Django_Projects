from django.db import models
from autoslug import AutoSlugField

class News(models.Model):
    project_title = models.CharField(max_length=50)
    project_desc = models.TextField(max_length=300)
    project_slug = AutoSlugField(populate_from='project_title', unique=True, null=True)

    def __str__(self):
        return self.project_title
