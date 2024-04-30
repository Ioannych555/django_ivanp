from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новыӣ'),
        ('Fixing', 'На исправлении'),
        ('Fixed', 'Исправлен'),
    ]
    PRIORITY_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.title


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Consideration', 'На рассмотрении'),
        ('Accepted', 'Принято'),
        ('Declined', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Consideration"
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.title
