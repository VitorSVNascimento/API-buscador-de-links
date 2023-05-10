from django.contrib import admin
from link.models import Link

class Links(admin.ModelAdmin):
    list_display = ('id','nome','url')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

# Register your models here.
admin.site.register(Link,Links)