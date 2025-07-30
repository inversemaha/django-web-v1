from django.db import models
from datetime import datetime
# Create your models here.

class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.TextField(max_length=200)
    category_slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category" , on_delete=models.SET_DEFAULT)
    series_summary = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField("date published", default=datetime.now)
    tutorial_series = models.ForeignKey(TutorialSeries, on_delete=models.CASCADE, null=True, blank=True)
    tutorial_slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title