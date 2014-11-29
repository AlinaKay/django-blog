from django.db import models
import datetime
from django.template.defaultfilters import slugify

class Post(models.Model):
	author=models.ForeignKey('auth.user')
	title=models.CharField(max_length=200)
	text=models.TextField()
	url=models.SlugField(max_length=200,blank=True)
	created_date=models.DateTimeField(default=datetime.datetime.now())
	published_date=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date=datetime.datetime.now()
		self.save()

	def save(self, *args, **kwargs):
		if self.url=='':
			self.url = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title
