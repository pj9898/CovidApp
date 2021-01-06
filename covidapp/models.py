from django.db import models

# Create your models here.
class User(models.Model):
	user = models.TextField(default=None)
	def _str_(self):
		return self.user
		