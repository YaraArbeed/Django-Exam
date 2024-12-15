from django.db import models
class Developer (models.Model):
  Name=models.CharField(max_length=100,null=False) 
                         
class Game(models.Model):
    Title=models.CharField(max_length=100,null=False)
    Developer=models.ForeignKey(Developer, on_delete=models.CASCADE)