from django.contrib import admin
from .models import Post, Comment, Upcoming, PostM, PostH, MComment, HComment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Upcoming)
admin.site.register(PostM)
admin.site.register(PostH)
admin.site.register(MComment)
admin.site.register(HComment)
