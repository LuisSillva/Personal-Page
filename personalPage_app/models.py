from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    quote = models.TextField(max_length=555)
    description = models.TextField(max_length=255)
    twitterUrl = models.URLField(blank=True, null=True)
    instagramUrl = models.URLField(blank=True, null=True)
    githubUrl = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
