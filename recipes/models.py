# recipes/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
  title = models.TextField(blank=False, max_length=300)
  
  description = models.TextField(blank=True)
  
  recipe_image = models.FileField(upload_to='recipe_photoes', blank=True)
  
  ingredients = models.TextField(default=' ', blank=False)
  
  instructions = models.TextField(default=' ', blank=False)
  
  time = models.CharField(default=' ', max_length=50)
  yields = models.CharField(default=' ', max_length=50)
  
  nutritions = models.TextField(default=' ', blank=True)
  
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def get_absolute_url(self):
      return reverse("recipes-detail", kwargs={"pk": self.pk})

  def __str__(self):
    return self.title