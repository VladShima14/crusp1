from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Project name')
    title = models.CharField(max_length=500, verbose_name='Project title')
    main_image = models.ImageField(upload_to='projects/%Y/%m/%d/', verbose_name="Main image")
    description = models.TextField(verbose_name='Project description')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='project', verbose_name='Project')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name="Image for content")

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
