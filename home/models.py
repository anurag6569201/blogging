from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class BlogModel(models.Model):
    image=models.ImageField(upload_to="blog_images")
    profileName=models.CharField(max_length=100)
    creationDate=models.DateTimeField()
    readingTime=models.IntegerField()

    basedOn=models.CharField(max_length=100)
    heading=models.CharField(max_length=100)
    visiting=models.CharField(max_length=100)
    basicContent=models.CharField(max_length=300)
    text=CKEditor5Field('Text', config_name='extends')


class TopicsModel(models.Model):
    topicName=models.CharField(max_length=100)
    iconBoxImageName=models.CharField(max_length=100)

class TagsModel(models.Model):
    tagName=models.CharField(max_length=100)
