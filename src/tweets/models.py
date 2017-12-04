# -*- coding: utf-8 -*-


# from __future__ import unicode_literals
from django.conf import settings
from django.db import models


class Tweet(models.Model):
	# cada tweet é associado a um user
	user      = models.ForeignKey(settings.AUTH_USER_MODEL)
	content   = models.CharField(max_length=140)
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)