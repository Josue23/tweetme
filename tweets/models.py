	# -*- coding: utf-8 -*-

# from __future__ import unicode_literals
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from .validators import validate_content



class Tweet(models.Model):
	# cada tweet é associado a um user
	user      = models.ForeignKey(settings.AUTH_USER_MODEL)
	content   = models.CharField(max_length=140, validators=[validate_content])
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)

	# # # validation
	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == "abc":
	# 		raise ValidationError("Content cannot be ABC")
	# 	return super(Tweet, self).clean(*args, **kwargs)