from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class DailyKarmaType(models.TextChoices):
    PRAYER = "pr", _("Prayer")
    STUDY = "st", _("Study")
    WORK = "wo", _("Work")
    FAMILY = "ho", _("Home")
    PUBLIC = "pu", _("People")
    PLAY = "pl", _("Play")


class DailyKarmaReview(models.TextChoices):
    PENDING = "pe", _("Pending")
    SATISFIED = "sa", _("Satisfied")
    UNSATISFIED = "us", _("Unsatisfied")
        

class DailyKarma(models.Model):
    """
        Represents daily routines like Puja, Study, etc.
        Every karma is either type daily(prayer, regular)
        Every karma has three possible state - Pending, Good, Bad
    """
    title = models.CharField(max_length=32)
    karma = models.CharField(max_length=128)
    date = models.DateField()
    type = models.CharField(
         max_length=2,
         choices=DailyKarmaType.choices,
         default=DailyKarmaType.STUDY
    )    
    review = models.CharField(
        max_length=2, 
        choices= DailyKarmaReview.choices,
        default=DailyKarmaReview.PENDING
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_review_display_name(self):
        return self.get_review_display()
    
    def __str__(self):
        return f"{self.get_review_display_name()}, {self.karma:20}, {self.date}"
    

class DayReview(models.Model):
    """
        Add a review for how the day went on a day-to-day basis
    """
    review = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Review: {self.review:20}"


class Reflection(models.Model):
    """
        Add reflection for the day
    """
    reflection = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.date}, Reflection: {self.reflection:20}"