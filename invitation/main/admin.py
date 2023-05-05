from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Wedding, WeddingPhotos


class WeddingPhotosInline(admin.TabularInline):
    model = WeddingPhotos
    fk_name = 'post'
    fields = ('photos', 'get_html_photo')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.photos:
            return mark_safe(f"<img src='{object.photos.url}' width=100>")
    get_html_photo.short_description = 'Миниатюра'


class WeddingAdmin(admin.ModelAdmin):
    model = Wedding
    inlines = [WeddingPhotosInline, ]


admin.site.register(Wedding, WeddingAdmin)
