import logging
import uuid

from django.core.validators import MinValueValidator
from django.db import models

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

    line = models.CharField(max_length=15, choices=LINE_CHOICES)
    cost = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.line}"


class Call(models.Model):
    """
    Our call models objects are created here and stored in the database
    as a table with the attributes mentioned below.
    """

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

    objects = models.Manager()
    search = SearchManager()

    def save(self, *args, **kwargs):
        """
        Here we over-ride the default `save` method to populate the cost field
        based on call duration and call type.
        """
        if self.duration <= 0:
            return
        elif self.type.type == "Domestic":
            self.cost = self.type.cost  # Since domestic calls have fixed value
        else:
            self.cost = (
                self.type.cost * self.duration
            )  # for national and international calls
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return f"{self.category.line} call of {self.duration} seconds"
