from django.db import models

class MainPageImage (models.Model):
    image = models.TextField()

class Introduction (models.Model):
    introduction = models.TextField()
    

class MainPage (models.Model):
    experience = models.TextField()
    startdate = models.TextField()
    enddate = models.TextField()
    experiencedesc = models.TextField()

class PhotoGrid(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    project_url = models.URLField()

    def __str__(self):
        return self.title
        
class SocialPlatform(models.Model):
    name = models.CharField(max_length=100)  # Platform name (e.g., Twitter, Instagram)
    description = models.TextField(blank=True, null=True)  # Optional description
    url = models.URLField()  # Profile link
    logo = models.ImageField(upload_to='platform_logos/', blank=True, null=True)  # Platform logo

    def __str__(self):
        return self.name
# Create your models here.
