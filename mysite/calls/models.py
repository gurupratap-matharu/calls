from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone



class Type(models.Model):
    """
    We define the type of call - domestic, national or international in this class. This gives us the freedom to change their rates in the admin.
    """
    CALL_CHOICES = (
        ('International', 'International'),
        ('National', 'National'),
        ('Domestic', 'Domestic'),
    )

    type = models.CharField(max_length=15, choices=CALL_CHOICES)
    cost = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.type

class Call(models.Model):
    """
    Our call models objects are created here and stored in the database
    as a table with the attributes mentioned below.
    """

    duration = models.PositiveIntegerField('Call duration in seconds', validators=[MinValueValidator(1)], default=1)
    type = models.ForeignKey(Type,on_delete=models.CASCADE,default=None)
    cost = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        """
        Here we over-ride the default `save` method to populate the cost field
        based on call duration and call type.
        """
        if self.duration <= 0:
            return
        elif self.type.type == "Domestic":
            self.cost = self.type.cost # Since domestic calls have fixed value
        else:
            self.cost = self.type.cost * self.duration # for national and international calls
        super().save(*args, **kwargs)  # Call the "real" save() method.


    def __str__(self):
        return "{} call of {} seconds".format(self.type.type, self.duration)

