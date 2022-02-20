from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Activity(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    TYPE_CHOICES = [
        (0, "Unspecified"),
        (1, "Project"),
        (2, "Task"),
        (3, "Event"),
        (4, "Tradeshow"),
        (5, "Research"),
    ]
    state = models.IntegerField(
        default=1,
        choices=TYPE_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.id)

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return str(self.id)

    class Meta:
        ordering = ["-start_date"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        unique_together = ("name", "code")

    def preview(self):
        return self.description[:100]

    def start_date_pretty(self):
        if self.start_date:
            return self.start_date.strftime("%d %b %Y")
        else:
            return None

    def end_date_pretty(self):
        if self.end_date:
            return self.end_date.strftime("%d %b %Y")
        else:
            return None
