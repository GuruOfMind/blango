from django.contrib import admin
from blog.models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ("slug", "published_at")
# exclude : list of fields disallowed to edit in the admin
# fields  : opposite of exclude
# list_display: a list of fields to include in the admin page list view

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)