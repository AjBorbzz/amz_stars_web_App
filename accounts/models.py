from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class AMZStar(models.Model):
    account_manager = 'Account Manager'
    customer_support = 'Customer Support Representative'
    JOB_TITLE = [(account_manager, 'Account Manager'),
                 (customer_support, 'Customer Support Representative')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50, choices=JOB_TITLE)
    date_joined = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
