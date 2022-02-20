from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Resource(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    TYPE_CHOICES = [
        (0, "Unspecified"),
        (1, "Employee"),
        (2, "Team"),
        (3, "Contractor"),
    ]
    state = models.IntegerField(
        default=1,
        choices=TYPE_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        blank=True,
        null=True,
    )
    comment = models.TextField(blank=True, null=True)
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
        ordering = ["name", "surname", "-updated_at"]
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        unique_together = ("name", "surname")

    def preview(self):
        return self.comment[:100]
