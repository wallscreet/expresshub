from django.contrib import admin
from .models import Post, Comment, Upcoming

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Upcoming)
