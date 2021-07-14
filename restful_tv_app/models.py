from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 1:
            errors["title"] = "Title should be at least 1 Character."
        if len(postData['network']) < 1:
            errors["network"] = "Network should be at least 1 Character."
        if len(postData['date']) < 1:
            errors["date"] = "Please enter a valid date"
        if len(postData['description']) < 1:
            errors["description"] = "Description should be at least 1 Character."
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    objects = ShowManager()
