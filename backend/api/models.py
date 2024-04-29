from django.db import models
from django.contrib.auth.models import User
        
class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    trip_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Suggestion(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='suggestions', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suggestions', null=True, blank=True)
    prompt = models.TextField()
    content = models.TextField()
    role = models.CharField(max_length=50)
    model_used = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
