import sys
import os
import django
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_forum.settings') 
django.setup()

from forum.models import Project, Comments

project_1 = Project.objects.create(title = "тест project", description = "first description in project")
comment_1 = Comments.objects.create(project = project_1, contet = "first comment_test")