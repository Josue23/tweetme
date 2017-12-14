	# -*- coding: utf-8 -*-

# from __future__ import unicode_literals
from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models

from .validators import validate_content



class Tweet(models.Model):
	# cada tweet é associado a um user
	# pk = Tweet.objects.get(pk=id)
	user      = models.ForeignKey(settings.AUTH_USER_MODEL)
	content   = models.CharField(max_length=140, validators=[validate_content]) # different validations
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)

	# get_absolute_url é chamado quando cria um novo objeto no banco usando TweetCreateView em views.py
	def get_absolute_url(self):
		return reverse('tweet:detail', kwargs={'pk': self.pk})

	# # # validation
	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == "abc":
	# 		raise ValidationError("Content cannot be ABC")
	# 	return super(Tweet, self).clean(*args, **kwargs)