from django.contrib import admin

from cms.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,PostAdmin)