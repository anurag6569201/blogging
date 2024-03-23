from django.contrib import admin
from .models import BlogModel,TopicsModel,TagsModel


admin.site.register(BlogModel)
admin.site.register(TopicsModel)
admin.site.register(TagsModel)
