from django.contrib import admin
from manager.models import landingpagecontent

# Register your models here.

class managelandingpagecontent(admin.ModelAdmin):
    list_display=['img', 'imageheading', 'imagedex']

admin.site.register(landingpagecontent, managelandingpagecontent)