from django.contrib import admin
from .models import image
from .models import info
# Register your models here.
@admin.register(image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo']


admin.site.register(info)