# -*- coding: utf-8 -*-


# from __future__ import unicode_literals

from django.db import models


class Tweet(models.Model):
	# user
	content   = models.CharField(max_length=140)
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)