from django.contrib import admin

# Register your models here.
from myblog.models import Article, Tag
admin.site.register(Tag)
admin.site.register(Article)
