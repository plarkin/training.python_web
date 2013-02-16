#ideas: http://lightbird.net/dbe/blog.html, https://github.com/ilblackdragon/django-blogs/blob/master/blog/models.py 

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Entry(models.Model):
	publication_date = models.DateTimeField('Date Published')
	author = 
	title = models.CharField(max_length=80)

	def __unicode__(self):
		return self.title