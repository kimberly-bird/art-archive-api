from django.db import models


class Artist(models.Model):
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  dob = models.CharField(max_length=10)
  death_date = models.CharField(max_length=10, default="")

  def __str__(self):
    return "{} {}".format(self.user.first_name, self.user.last_name)

