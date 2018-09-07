from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    current_location = models.CharField(max_length=300)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

