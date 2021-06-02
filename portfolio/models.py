from django.db import models
import ast

class Project(models.Model):
    name = models.CharField(max_length=100)
    key_points = models.TextField(default='[]')
    description = models.TextField()
    language_icons = models.TextField(default='[]')
    deployment_icons = models.TextField(default='[]')

    def getProjects():
        projects = Project.objects.all()
        for project in projects:
            # eval to list
            project.key_points = ast.literal_eval(project.key_points)
            project.language_icons = ast.literal_eval(project.language_icons)
            project.deployment_icons = ast.literal_eval(project.deployment_icons)
        return projects

        

