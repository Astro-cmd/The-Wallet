from django.db import models
from users.models import User
import string

# Create your models here.
class Goals:
    goal_id = models.CharField(primary_key= True, max_length= 18, )
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True, related_name='goals')
    name = models.CharField(max_length=100,null = False, blank= False)
    Due_date = models.DateTimeField()
    description = models.TextField(max_length=500, blank=True, null=True)
    priority = models.CharField(max_length = 25, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ])
    status = models.CharField(max_length=25, choices=[
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ])
    created_at = models.DateField(auto_now_add=True)
   
    updated_at = models.DateField(auto_now=True)
    
    
    class Meta:
        verbose_name_plural = "goals"

    def __str__(self):
         return self.name
    
