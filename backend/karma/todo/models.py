from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class TodoStatus(models.TextChoices):
    TODO = "to", _("Todo")
    PROGRESS = "pr", _("Progress")
    COMPLETE = "co", _("Complete")
    ARCHIVED = "ar", _("Archived")


class TodoType(models.TextChoices):
    PRAYER = "pr", _("Prayer")
    STUDY = "st", _("Study")
    WORK = "wo", _("Work")
    FAMILY = "ho", _("Home")
    PUBLIC = "pu", _("People")
    PLAY = "pl", _("Play")


class Todo(models.Model):
    """
        Represents tasks with todo, in-progress, complete status
    """
    todo = models.CharField(max_length=100)
    todo_type = models.CharField(
        max_length=2,
        choices=TodoType.choices,
        default=TodoType.STUDY
    )
    status = models.CharField(
        max_length=2,
        choices=TodoStatus.choices,
        default=TodoStatus.TODO
    )
    created_on = models.DateField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed_on = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_todo_type_display_name(self):
        return self.get_todo_type_display()

    def __str__(self):
        return f"{self.todo} - {self.get_todo_type_display_name()}"