from django.contrib import admin
from .models import BlogModel,TopicsModel,TagsModel,MainBlogModel


admin.site.register(BlogModel)
admin.site.register(TopicsModel)
admin.site.register(TagsModel)
admin.site.register(MainBlogModel)
