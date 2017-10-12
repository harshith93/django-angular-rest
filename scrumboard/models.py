# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class List(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return 'List: {}'.format(self.name)

@python_2_unicode_compatible
class Card(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    list = models.ForeignKey(List, related_name="cards")
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'Card: {}'.format(self.title)

