from datetime import date
from math import remainder
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.


class UserList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1250, blank=True)
    remainderDate = models.DateField(
        validators=[MinValueValidator(date.today(), message="Invalid Date")]
    )
    remainderTime = models.TimeField()
    remainder = models.BooleanField(default=False)
    date_time_added = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return self.title
