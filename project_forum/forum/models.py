from django.db import models
import uuid


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField() # поле с описанием

    def __str__(self) -> str: # метод возвращает title
        return self.title


class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # уникальный номер таблицы
    contet = models.TextField() # сам комментарий
    created_at = models.DateTimeField(auto_now_add=True) # дата создания записи (комментария)
    project = models.ForeignKey(
        Project, related_name="comments", on_delete=models.CASCADE
    ) # поле таблицы, которе ссылется на Project

    def __str__(self) -> str: # возвращает опиасние
        return f"Comment on {self.project.title}"
    