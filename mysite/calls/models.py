import logging
import uuid

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

logger = logging.getLogger(__name__)


class SearchManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def search(self, q):
        logger.info("searching by %s" % q)
        return


class Category(models.Model):
    """
    Type of call - domestic, national or international in this class.
    This gives us the freedom to change their rates in the admin.
    """

    INTERNATIONAL = "I"
    NATIONAL = "N"
    DOMESTIC = "D"

    LINE_CHOICES = (
        (INTERNATIONAL, "International"),
        (NATIONAL, "National"),
        (DOMESTIC, "Domestic"),
    )

    line = models.CharField(max_length=2, choices=LINE_CHOICES, unique=True)
    cost = models.DecimalField(
        verbose_name="Cost per second",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.get_line_display()


class Call(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    duration = models.PositiveIntegerField(
        "Call duration in seconds", validators=[MinValueValidator(1)], default=1
    )
    category = models.ForeignKey(
        "calls.Category", on_delete=models.CASCADE, related_name="calls"
    )
    cost = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    search = SearchManager()

    class Meta:
        verbose_name = "call"
        verbose_name_plural = "calls"
        ordering = ("-created_on",)

    def save(self, *args, **kwargs):
        """
        Here we over-ride the default `save` method to populate the cost field
        based on call duration and call category price.
        """

        self.cost = self.category.cost * self.duration
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.get_line_display()} call of {self.duration} seconds"

    def get_absolute_url(self):
        return reverse("calls:call-detail", kwargs={"pk": self.id})
