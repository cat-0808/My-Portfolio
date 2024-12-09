from django.contrib import admin
from .models import MainPage, Introduction, MainPageImage, PhotoGrid, SocialPlatform

admin.site.register(MainPage)
admin.site.register(Introduction)
admin.site.register(MainPageImage)
admin.site.register(PhotoGrid)
admin.site.register(SocialPlatform)

class SocialPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')  # Show platform name and URL
    search_fields = ('name',)  # Allow search by name
    ordering = ('name',)  # Order by name

class PhotoGridAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project_url')
# Register your models here.
