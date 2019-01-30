from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db import models


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
    cost = models.FloatField(default=0)
    
    def __str__(self):
        return self.type

class Call(models.Model):
    """
    Our call models objects are created here and stored in the database
    as a table with the attributes mentioned below.
    """
        
    duration = models.PositiveIntegerField('Call duration in seconds', validators=[MinValueValidator(1)], default=1)
    type = models.ForeignKey(Type,on_delete=models.CASCADE,default=None)
    
    @property
    def calculateCost(self):
        """
        Calculates the total cost of the call based on call type and call duration.
        """
        if (self.type.type == 'Domestic'):
            
            return self.type.cost

        else:
            return self.type.cost * self.duration


    def __str__(self):
        return "{} call of {} seconds".format(self.type.type, self.duration)
        