from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class BlogModel(models.Model):
    image=models.ImageField(upload_to="blog_images")
    profileName=models.CharField(max_length=100)
    creationDate=models.DateTimeField()
    readingTime=models.IntegerField()

    basedOn=models.CharField(max_length=100)
    heading=models.CharField(max_length=100)
    basicContent=models.CharField(max_length=300)

class TopicsModel(models.Model):
    topicName=models.CharField(max_length=100)
    iconBoxImageName=models.CharField(max_length=100)

class TagsModel(models.Model):
    tagName=models.CharField(max_length=100)