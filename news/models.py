from django.db import models

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=128)
    url = models.TextField()
    url_to_image = models.TextField(name='urlToImage')
    image = models.ImageField(upload_to = 'photos' , null = True)
    published_at = models.DateTimeField(name= 'publishedAt')

