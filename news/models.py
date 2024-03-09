from django.db import models

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=128)
    url = models.TextField()
    url_to_image = models.TextField(name='urlToImage')
    published_at = models.CharField(max_length=64 , name= 'publishedAt')
    content = models.TextField()
    category = models.CharField(max_length=64)

