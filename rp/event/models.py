from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from rp.activity.models import Activity
from rp.resource.models import Resource


class Event(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    resource = models.ForeignKey(
        Resource, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    activity = models.ForeignKey(
        Activity, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    COMMIT_CHOICES = [
        (100, "Full"),
        (75, "Dedicated"),
        (50, "Partial"),
        (25, "Light"),
        (10, "Limited"),
        (0, "None"),
    ]
    commit = models.IntegerField(
        verbose_name="Commitment",
        default=100,
        choices=COMMIT_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
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
        verbose_name = "Event"
        verbose_name_plural = "Events"

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
